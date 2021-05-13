H, W = map(int, input().split())

grid = [input() for _ in range(H)]
# print(grid)

dp = [[0 for _ in range(W + 1)]for _ in range(H + 1)]
# print(dp)

dp[1][1] = 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if not (i == 1 and j == 1):
            if grid[i - 1][j - 1] == "#":
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10**9 + 7)

# print(dp)
ans = dp[-1][-1]
print(ans)
