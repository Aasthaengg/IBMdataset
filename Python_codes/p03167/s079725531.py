H, W = map(int, input().split(" "))
m = [list(input().strip()) for _ in range(H)]
mod = 10**9 + 7

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        if h+1 < H and m[h+1][w] == ".":
            dp[h+1][w] += dp[h][w]
            dp[h+1][w] %= mod
        if w+1 < W and m[h][w+1] == ".":
            dp[h][w+1] += dp[h][w]
            dp[h][w+1] %= mod

print(dp[H-1][W-1])