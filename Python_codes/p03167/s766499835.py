H, W = map(int, input().split())
grid = [input() for i in range((H))]
dp = [[0 for i in range(W)] for j in range(H)]
dp[0][0] = 1
m = 10**9 + 7
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            continue
        if i >= 1:
            dp[i][j] += dp[i-1][j]
        if j >= 1:
            dp[i][j] += dp[i][j-1]

        dp[i][j] %= m

print(dp[-1][-1])