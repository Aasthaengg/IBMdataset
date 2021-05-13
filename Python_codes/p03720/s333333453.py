def resolve():
    from collections import defaultdict
    N, M = [int(i) for i in input().split()]
    aabb = [list(map(int, input().split())) for _ in range(M)]
    d = defaultdict(int)
    for a, b in aabb:
        d[a] += 1
        d[b] += 1
    for i in range(1, N + 1):
        print(d[i])


resolve()
