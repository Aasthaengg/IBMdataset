n, m = map(int, input().strip().split())
grid = []
for i in range(n):
    grid.append(input())
dp = [[None]*m for _ in range(n)]
dp[n-1][m-1] = 1
for i in range(n-2, -1, -1):
    if grid[i][m-1] == '.':
        dp[i][m-1] = dp[i+1][m-1]
    else:
        dp[i][m-1] = 0
for j in range(m-2, -1, -1):
    if grid[n-1][j] == '.':
        dp[n-1][j] = dp[n-1][j+1]
    else:
        dp[n-1][j] = 0
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        if grid[i][j] == '.':
            dp[i][j] = (dp[i+1][j] + dp[i][j+1])%(10**9 + 7)
        else:
            dp[i][j] = 0
print(dp[0][0])