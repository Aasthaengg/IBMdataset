n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[float('inf')]*50010 for _ in range(25)]
dp[0][0] = 0
for i in range(m):
    for j in range(n+1):
        if j >= c[i]:
            dp[i+1][j] = min(dp[i][j-c[i]] + 1, dp[i][j], dp[i+1][j-c[i]]+ 1)
        else:
            dp[i+1][j] = dp[i][j]

print(dp[m][n])
