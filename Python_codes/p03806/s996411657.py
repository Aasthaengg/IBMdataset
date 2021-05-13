N, Ma, Mb = map(int, input().split())

INF = 10 ** 18
dp = [[[INF] * (10*N+1) for _ in range(10*N+1)] for _ in range(N+1)]

dp[0][0][0] = 0
for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(10*N+1-a):
        for k in range(10*N+1-b):
            if dp[i][j][k] == INF:
                continue
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            dp[i+1][j+a][k+b] = min(dp[i+1][j+a][k+b], dp[i][j][k]+c)

ans = INF
for j in range(1, 10*N+1):
    if j * Ma > 10 * N  or j * Mb > 10 * N:
        break

    ans = min(ans, dp[N][j*Ma][j*Mb])

if ans == INF:
    ans = -1

print(ans)