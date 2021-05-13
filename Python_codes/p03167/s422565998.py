H, W = map(int, input().split())
g = [list(input()) for _ in range(H)]
mod = int(1e9) + 7
dp = [[0 for i in range(W)] for j in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if g[i][j] == "#":
            continue
        if i + 1 < H:
            dp[i+1][j] += dp[i][j] % mod
        if j + 1 < W:
            dp[i][j+1] += dp[i][j] % mod
print(dp[H-1][W-1] % mod)