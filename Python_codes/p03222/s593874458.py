
H, W, K = map(int, input().split())

MOD = 10 ** 9 + 7
dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for k in range(1 << (W - 1)):
            # Check valid connection
            ok = True
            for l in range(W - 2):
                if (k >> l) & 1 and k >> (l + 1) & 1:
                    ok = False

            if not ok:
                continue

            if j > 0 and k >> (j - 1) & 1:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
            elif j < W - 1 and k >> j & 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
            else:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD

print(dp[-1][K - 1])
