MOD = int(1e9) + 7
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
dp = [[0 for i in range(W)] for j in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i + 1 < H and maze[i+1][j] == ".":
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
        if j + 1 < W and maze[i][j+1] == ".":
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= MOD
print(dp[H-1][W-1])