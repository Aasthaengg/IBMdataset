n, m = map(int, input().split())

grid = [None]*n
mod = 10**9+7

for i in range(n):
    grid[i] = list(input())

dp = [[0]*m for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    if grid[i][0] != '#':
        dp[i][0] = 1
    else:
        break

for i in range(m):
    if grid[0][i] != '#':
        dp[0][i] = 1
    else:
        break

for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] == '#':
            continue

        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod

print(dp[-1][-1])