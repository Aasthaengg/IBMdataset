
H, W = map(int, input().split())
grid = []
d = [(1, 0), (0, 1)]
for _ in range(H):
    grid.append(input())
dp = [[0 for _ in range(W)] for _ in range(H)]
mod = 1e9 + 7
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        if h > 0 and grid[h - 1][w] == '.':
            dp[h][w] = (dp[h][w] + dp[h - 1][w]) % mod
        if w > 0 and grid[h][w - 1] == '.':
            dp[h][w] = (dp[h][w] + dp[h][w - 1]) % mod
print(int(dp[H - 1][W - 1]))
