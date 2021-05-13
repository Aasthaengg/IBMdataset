import sys
input = sys.stdin.readline
n, ma, mb = map(int, input().split())
inf = 10000
med = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[[inf] * 401 for _ in range(401)] for _ in range(n+1)]
dp[0][0][0] = 0
for k in range(n):
    for i in range(401):
        for j in range(401):
            a, b, c = med[k]
            if i - a >= 0 and j - b >= 0:
                dp[k+1][i][j] = min(dp[k][i][j], dp[k][i-a][j-b] + c)
            else:
                dp[k+1][i][j] = dp[k][i][j]

ans = inf
for k in range(1, 401):
    if k * ma > 400 or k * mb > 400:
        break
    x, y = k * ma, k * mb
    ans = min(ans, dp[n][x][y])

print(-1 if ans == inf else ans)
