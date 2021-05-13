H, W = map(int, input().split())
grid = [input() for _ in range(H)]
dp = [[float('inf')] * W for i in range(H)]
dp[0][0] = 1 if grid[0][0] == '#' else 0

for i in range(H):
    for j in range(W):
        for y, x in ((1,0), (0,1)):
            ni, nj = i + y, j + x
            if ni >= H or nj >= W:
                continue
            c = 0
            if grid[ni][nj] == '#' and grid[i][j] == '.':
                c = 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + c)

print(dp[H-1][W-1])