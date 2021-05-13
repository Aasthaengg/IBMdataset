def resolve():
    from collections import defaultdict
    N = int(input())
    A = [int(input()) for _ in range(N)]
    c = defaultdict(int)
    for a in A:
        c[a] += 1
    ans = 0
    for v in c.values():
        if v % 2 == 1:
            ans += 1
    print(ans)


resolve()
