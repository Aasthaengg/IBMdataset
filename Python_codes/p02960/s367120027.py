import sys
input = sys.stdin.readline

S = list(input()[:-1])
S.reverse()
dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(len(S)):
    p = pow(10, i, 13)
    
    if S[i]=='?':
        for j in range(10):
            for k in range(13):
                dp[i+1][(k+j*p)%13] += dp[i][k]
                dp[i+1][(k+j*p)%13] %= MOD
    else:
        for j in range(13):
            dp[i+1][(j+int(S[i])*p)%13] += dp[i][j]
            dp[i+1][(j+int(S[i])*p)%13] %= MOD

print(dp[len(S)][5])