mod = 10**9+7
s = input()
N = len(s)

dp = [[0]*13 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(13):
        if s[i] == '?':
            for x in range(10):
                dp[i+1][(10*j+x)%13] += dp[i][j]
                dp[i+1][(10*j+x)%13] %= mod
        else:
            x = int(s[i])
            dp[i+1][(10*j+x)%13] += dp[i][j]
            dp[i+1][(10*j+x)%13] %= mod

print(dp[N][5])