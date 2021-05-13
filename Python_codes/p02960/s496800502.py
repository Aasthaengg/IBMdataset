mod = 1000000007
    
S = list(input())

n = len(S)

dp = [[0]*13 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    s = S[i]
    for j in range(13):
        if s == '?':
            for k in range(10):
                dp[i+1][(j*10+k)%13] += dp[i][j]
        else:
            dp[i+1][(j*10+int(s))%13] += dp[i][j]
        dp[i+1][j] %= mod
print(dp[n][5]%mod)