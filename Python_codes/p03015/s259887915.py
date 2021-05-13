MOD = 10 ** 9 + 7
L = input()
N = len(L)

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    d = int(L[i])
    for j in range(2):
        D = 1 if (d == 1 or j == 1) else 0
        for a, b in [(1, 0), (0, 1), (0, 0)]:
            if a + b <= D:
                here = dp[i + 1][j | (a + b < D)]
                here = (here + dp[i][j]) % MOD
                dp[i + 1][j | (a + b < D)] = here

print((dp[N][0] + dp[N][1]) % MOD)
