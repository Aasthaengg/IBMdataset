N,M = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]+[0]
T = [int(x) for x in input().split()]+[0]
MOD = 10**9+7
dp=[[[0]*2 for _ in range(M+2)] for _ in range(N+2)]
dp[0][0][0]=1
for i in range(N+1):
    for j in range(M+1):
        dp[i+1][j][0] += dp[i][j][0]
        dp[i+1][j][0] %= MOD
        dp[i][j][1] += dp[i][j][0]
        dp[i][j][1] %= MOD
        dp[i][j+1][1] += dp[i][j][1]
        dp[i][j+1][1] %= MOD
        if(S[i]==T[j]):
            dp[i+1][j+1][0] += dp[i][j][1]
            dp[i+1][j+1][0] %= MOD

print(dp[N][M][1])
