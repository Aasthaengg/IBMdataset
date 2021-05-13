n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1][1] = 1
for i in range(0, n+1):
    for j in range(0, i+1):
        if i == 0 or j == 0 or i == j:
            dp[i][j] = 1
            continue

        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for i in range(1, k+1):
    print(dp[n-k+1][i]*dp[k-1][i-1]%(10**9+7))