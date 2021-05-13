S = input()
N = len(S)
MOD = 10**9+7
dp = [[0]*13 for _ in range(N+1)]
dp[0][0] = 1

base = 1
for i in range(N):
    if S[N-1-i] != '?':
        mi = int(S[N-1-i])*base
        mi %= 13
        for j in range(13):
            dp[i+1][(j+mi)%13] += dp[i][j]
            dp[i+1][(j+mi)%13] %= MOD
    else:
        for j in range(13):
            for k in range(10):
                Ti = base * k
                Ti %= 13
                dp[i+1][(j+Ti)%13] += dp[i][j]
                dp[i+1][(j+Ti)%13] %= MOD
    base *= 10
    base %= 13
print(dp[N][5])