N, T = map(int, input().split())
dishes = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
"""
dp[i][j]: 0~i番目までの料理でj分以内に完食できる美味しさの合計の最大値
"""
dp = [[0] * 3100 for _ in range(3100)]
ans = 0
for i in range(1, N+1):
    for j in range(1, T):
        dp[i][j] = dp[i-1][j]
        ans = max(ans, dp[i][j] + dishes[i-1][1])
        if j - dishes[i-1][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-dishes[i-1][0]] + dishes[i-1][1])

print(ans)
