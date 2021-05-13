def list2d(a, b, c): return [[c] * b for i in range(a)]
mod =10**9+7
H, W = map(int, input().split())

grid = []

for _ in range(H):
    grid.append(list(input()))

dp = list2d(H, W, 0)
for i in range(H-1, -1, -1):
    if(grid[i][W-1] == '#'):
        break
    dp[i][W-1] = 1

for j in range(W-1, -1, -1):
    if(grid[H-1][j]=='#'):
        break
    dp[H-1][j] = 1

for row in range(H-2, -1, -1):
    for col in range(W-2, -1, -1):
        if(grid[row][col] == '.'):
            dp[row][col] = (dp[row][col+1] + dp[row+1][col])%mod
        else:
            dp[row][col] = 0
print(dp[0][0]%mod)