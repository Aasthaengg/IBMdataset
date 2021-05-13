s = input()
mod = 10**9 + 7
n = len(s)
dp = [[0] * 13 for i in range(n+1)]
dp[0][0] = 1
for i in range(n):
    ss = s[i]
    for j in range(13):
        if ss == '?':
            for k in range(10):
                dp[i+1][(j*10+k)%13] += dp[i][j]
        else:
            dp[i+1][(j*10+int(ss))%13] += dp[i][j]
        dp[i+1][j] %= mod
print(dp[n][5]%mod)