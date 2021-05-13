S = list(input())
L = len(S)
M = 13
MOD = 10**9 + 7
dp = [[0]*M for _ in range(L+1)]
dp[0][0]=1
for i in range(L):
    p = pow(10, L-1-i, 13)
    if S[i] == "?":
        for j in range(M):
            for k in range(10):
                s = k*p
                dp[i+1][(j+s)%13] += dp[i][j]
                dp[i + 1][(j + s) % 13] %= MOD
    else:
        s = int(S[i])
        s *= p
        for j in range(M):
            dp[i+1][(j+s)%13] += dp[i][j]
            dp[i + 1][(j + s) % 13] %= MOD

print(dp[L][5])