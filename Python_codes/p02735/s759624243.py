h, w = map(int, input().split())
grid = []
for i in range(h):
    l = list(input())
    grid.append(l)

dp = [[0 for x in range(w)] for y in range(h)]
if grid[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(1, w):
    if grid[0][i] == '.':
        dp[0][i] = dp[0][i-1]
    else:
        if grid[0][i-1] == '.':
            dp[0][i] = dp[0][i-1]+1
        else:
            dp[0][i] = dp[0][i-1]

for i in range(1, h):
    if grid[i][0] == '.':
        dp[i][0] = dp[i-1][0]
    else:
        if grid[i-1][0] == '.':
            dp[i][0] = dp[i-1][0]+1
        else:
            dp[i][0] = dp[i-1][0]

for i in range(1, h):
    for j in range(1, w):
        if grid[i][j] == '.':
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        else:
            if grid[i-1][j] == '#' and grid[i][j-1] == '#':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            elif grid[i-1][j] == '#':
                dp[i][j] = dp[i-1][j]
            elif grid[i][j-1] == '#':
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[h-1][w-1])


