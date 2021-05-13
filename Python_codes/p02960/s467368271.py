def resolve():
    S = list(input())
    MOD = 10**9+7
    dp = [[0 for _ in range(13)] for __ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(13):
            if S[i] == "?":
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    if dp[i+1][(j*10+k)%13] > MOD:
                        dp[i+1][(j*10+k)%13] -= MOD
            else:
                k = int(S[i])
                dp[i+1][(j*10+k)%13] += dp[i][j]
                if dp[i+1][(j*10+k)%13] > MOD:
                    dp[i+1][(j*10+k)%13] -= MOD
    print(dp[len(S)][5])

if '__main__' == __name__:
    resolve()
