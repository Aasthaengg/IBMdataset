N = int(input())

grid = []

for i in range(N):
    grid.append([int(x) for x in input().split()])

dp = [[0]*3 for i in range(N)]
dp[0] = grid[0]

for i in range(1,N):
    for j in range(3):
        dp[i][j] = max(dp[i-1][k]+grid[i][j] for k in {0,1,2}-{j})

print(max(dp[:][N-1]))