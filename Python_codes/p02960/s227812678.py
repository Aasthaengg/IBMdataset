S = input()[::-1]
N = len(S)

mod = 10**9 + 7

dp = [[0]*13 for i in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    if S[i-1] == "?":
        for j in range(10):
            tmp_mod = (j * pow(10, i-1, 13)) % 13
            for k in range(13):
                dp[i][k] = (dp[i][k] + dp[i-1][k-tmp_mod%13]) % mod

    else:
        tmp_mod = (int(S[i-1]) * pow(10, i-1, 13)) % 13
        for k in range(13):
            dp[i][k] = (dp[i][k] + dp[i-1][k-tmp_mod%13]) % mod

print(dp[N][5])