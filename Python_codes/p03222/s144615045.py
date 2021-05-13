H, W, K = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [[0] * W for i in range(H + 1)]
dp[0][0] = 1
fib = [1, 2, 3, 5, 8, 13, 21, 34]


def calc(w):
    if w < 0:
        return 1
    return fib[w]


for h in range(H):
    for w in range(W):
        dp[h + 1][w] = (dp[h + 1][w] + dp[h][w] * calc(w - 1) * calc(W - w - 2)) % MOD
        if w + 1 < W:
            dp[h + 1][w + 1] = (dp[h + 1][w + 1] + dp[h][w] * calc(w - 1) * calc(W - w - 3) % MOD)
        if w - 1 >= 0:
            dp[h + 1][w - 1] = (dp[h + 1][w - 1] + dp[h][w] * calc(w - 2) * calc(W - w - 2) % MOD)

print(dp[H][K - 1] % MOD)
