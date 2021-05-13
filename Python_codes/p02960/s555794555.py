p = 10**9+7
S = input().strip()
N = len(S)
dp = [[0 for _ in range(13)] for _ in range(N+1)]
for m in range(13):
    dp[0][0] = 1
for i in range(1,N+1):
    for m in range(13):
        if S[i-1]=="?":
            for j in range(10):
                dp[i][(m*10+j)%13] = (dp[i][(m*10+j)%13]+dp[i-1][m])%p
        else:
            dp[i][(m*10+int(S[i-1]))%13] = (dp[i][(m*10+int(S[i-1]))%13]+dp[i-1][m])%p
print(dp[N][5])