S = input()
N = len(S)
MOD = 10**9 + 7
dp = [[0]*(N+1) for _ in range(13)]
#dp[j][i]: 上からiケタ目までみたときの13で割った余りがjである個数
dp[0][0] = 1

for i in range(0, N):
    if S[i] == "?":
        for j in range(0, 10):
            for k in range(0, 13):
                dp[(k*10+j)%13][i+1] += dp[k][i]
    else:
        j = int(S[i])
        for k in range(0, 13):
            dp[(k*10+j)%13][i+1] += dp[k][i]
    
    for k in range(0, 13):
        dp[k][i+1] %= MOD

print(dp[5][N]%MOD)