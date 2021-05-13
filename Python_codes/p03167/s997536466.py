grid = []
dp = []
h,w = [int(x) for x in input().split()]

for i in range(h):
    grid.append(input())
    dp.append([0]*w)

dp[-1][-1] = 1

for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if grid[i][j] == '#':
            continue

        if i+1 < h and grid[i+1][j] != '#':
            dp[i][j] += dp[i+1][j]
        if j+1 < w and grid[i][j+1] != '#':
            dp[i][j] += dp[i][j+1]

print(dp[0][0] % int(1e9+7))