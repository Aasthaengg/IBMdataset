from collections import defaultdict
N, C = map(int, input().split())
D = [[int(i) for i in input().split()] for _ in range(C)]

color = [[int(i) for i in input().split()] for _ in range(N)]
M = [defaultdict(int) for _ in range(3)]
for i in range(N):
    for j in range(N):
        M[(i+j) % 3][color[i][j]] += 1

ans = 10**20
for Y0 in range(C):
    for Y1 in range(C):
        for Y2 in range(C):
            if Y0 != Y1 and Y1 != Y2 and Y2 != Y0:
                Y = (Y0, Y1, Y2)
                d = 0
                for i in range(3):
                    for X, v in M[i].items():
                        d += D[X-1][Y[i]]*v
                ans = min(ans, d)
print(ans)
