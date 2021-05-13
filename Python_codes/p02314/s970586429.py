inf = 10**9+7
mod = 10**9+7
n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [[inf for j in range(n+1)]for i in range(m+1)] #i番目まででj払う時に必要な最小枚数
dp[0][0] = 0
for i in range(m):
    dp[i+1][0] = 0
    for j in range(n):
        if j+1-c[i] >= 0:
            dp[i+1][j+1] = min(dp[i][j+1], dp[i][j+1-c[i]]+1, dp[i+1][j+1-c[i]]+1)
        else:
            dp[i+1][j+1] = dp[i][j+1]
print(dp[m][n])
