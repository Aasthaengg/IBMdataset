H, W, K = [int(str) for str in input().strip().split()]

MOD = 1000000007

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        for bit in range(2 ** (W - 1)):
            if bit & (bit << 1):
                continue

            
            if w > 0 and bit & (1 << (w - 1)):
                dp[h + 1][w - 1] += dp[h][w]
                dp[h + 1][w - 1] %= MOD
            
            elif w < W - 1 and bit & (1 << w):
                dp[h + 1][w + 1] += dp[h][w]
                dp[h + 1][w + 1] %= MOD

            else:
                dp[h + 1][w] += dp[h][w]
                dp[h + 1][w] %= MOD

print(dp[H][K - 1])