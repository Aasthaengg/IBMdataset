N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
ab.sort()
C = 0
M = 0
for i in range(N):
    C += ab[i][1]
    if C >= K:
        print(ab[i][0])
        break