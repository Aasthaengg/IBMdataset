S = input()
N = len(S)
MOD = 10**9+7
dp = [[0]*(14) for i in range(100010)]
dp[0][0] = 1

for i in range(N):
    if S[i] == '?':
        c = -1
    else:
        c = int(S[i])
        
    for j in range(10):
        if c != -1 and c != j:
            continue
        else:
            for k in range(13):
                dp[i+1][(k*10+j)%13] += dp[i][k]
        
    for j in range(13):
        dp[i+1][j] %= MOD
        
print(dp[N][5])