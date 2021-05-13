mod = 10**9 + 7
S = input()

dp = [[0]*13 for _ in range(len(S)+1)]
dp[0][0] = 1

for i in range(len(S)):
    if S[i] != '?':
        for m in range(13):
            dp[i+1][(10*m+int(S[i])) % 13] += dp[i][m]
            dp[i+1][(10*m+int(S[i])) % 13] %= mod
    else:
        for c in range(10):
            for m in range(13):
                dp[i+1][(10*m+c) % 13] += dp[i][m]
                dp[i+1][(10*m+c) % 13] %= mod

print(dp[len(S)][5])
