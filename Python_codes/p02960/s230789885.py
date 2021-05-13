"""
dp[i][j] => 下からi桁目まで見る。あまりがjになるような数。
"""
mod = 10**9 +7
S = input()
S = S[::-1]
N = len(S)
dp = [[0]*13 for _ in range(N+1)]
dp[0][0] = 1
by = 1
for i in range(N):
    s = S[i]
    for j in range(13):
        if s == "?":
            for k in range(10):
                rest = k*by%13
                dp[i+1][(j+rest)%13] += dp[i][j]
                dp[i+1][(j+rest)%13] %= mod
        else:
            rest = int(s)*by%13
            dp[i+1][(j+rest)%13] += dp[i][j]
            dp[i+1][(j+rest)%13] %= mod
    by = by*10%13
print(dp[-1][5])