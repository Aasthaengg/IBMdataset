S = input()
S = S[::-1]
MOD = 10**9 + 7

# dp[i][j]: i桁目までで，余りがjになるものの場合の数 
dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1

for i in range(len(S)):
    pow10 = pow(10,i,13)
    if S[i] != '?':
        d = int(S[i])
        for r in range(13):
            dp[i+1][(r + d*pow10) % 13] = dp[i][r]
    else:
        for d in range(10):
            for r in range(13):
                dp[i+1][(r + d*pow10) % 13] += dp[i][r]
                dp[i+1][(r + d*pow10) % 13] %= MOD

print(dp[len(S)][5])