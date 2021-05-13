n,s = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353
dp = [[0 for i in range(s+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1,n+1):
    x = a[i-1]
    for j in range(s+1):
        dp[i][j] = dp[i-1][j] * 2
        if dp[i][j] >= mod:
            dp[i][j] %= mod
    for j in range(x,s+1):
        if j >= x:
            dp[i][j] += dp[i-1][j-x]
            if dp[i][j] >= mod:
                dp[i][j] %= mod

print(dp[-1][-1])