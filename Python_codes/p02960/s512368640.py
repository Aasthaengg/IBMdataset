S = input()
N = len(S)
mod = 10**9+7
dp = [[0] * N for _ in range(13)]

if S[0] == "?":
    for i in range(10):
        dp[i][0] = 1
else:
    dp[int(S[0])][0] = 1
        
for i in range(1, N):
    if S[i] == "?":
        for s in range(10):
            for x in range(13):
                dp[(x*10 + s)%13][i] += dp[x][i-1]
    else:
        for x in range(13):
            dp[(x*10 + int(S[i]))%13][i] += dp[x][i-1] 
    for t in range(13):
        dp[t][i] = dp[t][i]%mod
print(dp[5][N-1])  