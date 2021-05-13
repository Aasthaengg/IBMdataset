n,s = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353
dp = [[0]*(s+1) for i in range(n+1)]
dp[1][0] = 2
if a[0] <= s:
    dp[1][a[0]] = 1
for i in range(2,n+1):
    for j in range(0,s+1):
        dp[i][j] = dp[i-1][j]*2
        if j-a[i-1] >= 0:
            dp[i][j] += dp[i-1][j-a[i-1]]
        dp[i][j] %= mod
print(dp[n][s])
