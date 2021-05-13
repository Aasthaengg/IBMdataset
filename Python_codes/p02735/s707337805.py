h,w = map(int,input().split())
grid = []
for _ in range(h):
    grid.append(input())
dp = [[float("inf") for _ in range(w)] for _ in range(h)]
if grid[0][0] == ".":
    dp[0][0] = 0
else:
    dp[0][0] = 1
for j in range(1,w):
    if grid[0][j-1] == "." and grid[0][j] == "#":
        dp[0][j] = dp[0][j-1] +1
    else:
        dp[0][j] = dp[0][j-1]
for i in range(1,h):
    for j in range(w):
        if j == 0:
            if grid[i-1][j] == "." and grid[i][j] == "#":
                dp[i][j] = dp[i-1][j]+1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if grid[i-1][j] == "." and grid[i][j-1] == "." and grid[i][j] == "#":
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
            elif grid[i][j-1] == "." and grid[i][j] == "#":
                dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j])
            elif grid[i-1][j] == "." and grid[i][j] == "#":
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]+1)
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])
print(dp[h-1][w-1])