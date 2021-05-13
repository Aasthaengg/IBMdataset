H, W, K = map(int, input().split())
MOD = 10**9 + 7

dp = [[0 for w in range(W)] for h in range(H + 1)]
dp[0][0] = 1


for h in range(H):
    for i in range(2 ** (W-1)):
        if '11' in bin(i):
            continue
        for w in range(W):  # このループが一番のポイント
            if w == 0:
                if (i >> w) & 1:
                    dp[h+1][w] += dp[h][w+1]
                else:
                    dp[h+1][w] += dp[h][w]
            elif 1 <= w < W-1:
                if (i >> (w-1)) & 1:
                    dp[h+1][w] += dp[h][w-1]
                elif (i >> w) & 1:
                    dp[h+1][w] += dp[h][w+1]
                else:
                    dp[h+1][w] += dp[h][w]
            else:
                if (i >> (w-1)) & 1:
                    dp[h+1][w] += dp[h][w-1]
                else:
                    dp[h+1][w] += dp[h][w]
            dp[h+1][w] %= MOD

print(dp[H][K-1])
