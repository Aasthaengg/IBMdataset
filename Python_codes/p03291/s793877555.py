MOD = 10 ** 9 + 7
S = input()
N = len(S)

dp = [[0] * 4 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(4):
        s = S[i]
        m1 = 3 if s == '?' else 1
        m2 = 1 if j != 0 and (s == '?' or s == 'ABC'[j - 1]) else 0
        dp[i + 1][j] = (m1 * dp[i][j] + m2 * dp[i][j - 1]) % MOD

print(dp[N][3])
