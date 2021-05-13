def resolve():
    N, M = [int(i) for i in input().split()]
    aabb = [list(map(int, input().split())) for _ in range(N)]
    ccdd = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        a, b = aabb[i]
        minPoint = -1
        minV = 10**9
        for j in range(M):
            c, d = ccdd[j]
            v = abs(a - c) + abs(b - d)
            if v < minV:
                minPoint = j + 1
            minV = min(minV, v)
        print(minPoint)


resolve()
