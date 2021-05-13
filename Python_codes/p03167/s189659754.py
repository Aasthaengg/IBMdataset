H, W = map(int, input().split())
grid = [list('#' * (W+1))]
for _ in range(1, H+1):
    temp = list(input())
    temp = ['#'] + temp
    grid.append(temp)
dp = [[0] * (W+1) for _ in range(H+1)]
dp[0][1] = 1
mod = 10**9 + 7

for i in range(1, H+1):
    for j in range(1, W+1):

        if grid[i][j] == '.':
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            dp[i][j] %= mod
            
print(dp[H][W])     