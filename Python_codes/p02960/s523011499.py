MOD = 10**9+7
S = input()
dp = [[0]*13 for i in range(len(S))]


if S[0]=='?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(S[0])] = 1

for i,c in enumerate(S[1:]):
    for j in range(13):
        if c=='?':
            for k in range(10):
                nj = (j*10 + k) % 13
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD
        else:
            nj = (j*10 + int(c)) % 13
            dp[i+1][nj] += dp[i][j]
            dp[i+1][nj] %= MOD

print(dp[-1][5])
