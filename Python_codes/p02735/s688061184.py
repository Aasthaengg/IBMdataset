h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]

dp = [[10000]*w for _ in range(h)]
dp[0][0] = 0 if grid[0][0] == "." else 1

for i in range(h):
    for j in range(w):
        if i > 0:
            if grid[i][j] == "#" and grid[i-1][j] == ".":
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j > 0:
            if grid[i][j] == "#" and grid[i][j-1] == ".":
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[h-1][w-1])