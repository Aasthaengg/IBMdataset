H, W = map(int, input().split())
inf = 10**9+7
maze = [list(input()) for i in range(H)]
dp = [[0 for i in range(W+1)] for j in range(H+1)]

#dp[i+1][j+1]:maze[i][j]に至るまでの方法の数
#dp[0][0] = 1
#dp[i][j] = dp[i][j-1] + dp[i-1][j]

dp[1][1] = 1
maze[0][0] = '#' #こうすると都合がいい
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]

print(dp[H][W] % inf)