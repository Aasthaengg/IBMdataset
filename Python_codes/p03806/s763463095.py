n, ma, mb = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(n)]

INF = 40 * 100 + 1
ab_max = 10 * n

dp = [[[INF] * (ab_max + 1) for _ in range(ab_max + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i, (a, b, c) in enumerate(abc, 1):
    for j in range(ab_max + 1):
        for k in range(ab_max + 1):
            dp[i][j][k] = dp[i-1][j][k]
            if j - a >= 0 and k - b >= 0:
                if dp[i-1][j-a][k-b] != INF:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-a][k-b] + c)


ans = INF
for j in range(1, ab_max + 1):
    for k in range(1, ab_max + 1):
        if j * mb == k * ma:
            ans = min(ans, dp[n][j][k])

if ans == INF:
    ans = -1

print(ans)
