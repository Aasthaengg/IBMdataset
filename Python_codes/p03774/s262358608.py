N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for a, b in ab:
    L = 10 ** 9
    p = 0
    i = 1
    for c, d in cd:
        l = abs(a - c) + abs(b - d)
        if l < L:
            L = l
            p = i
        i += 1
    print(p)
