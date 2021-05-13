h,w = map(int,input().split())
grid = ["#"*(w+1)]
for _ in range(h):
    x = input()
    x = "#" + x
    grid.append(x)
p = 10**9 + 7
dp = [[0]*(w+1) for _ in range(h+1)]
dp[1][1] =1
for i in range(h):
    for j in range(w):
        if grid[i][j+1] == ".":
            dp[i+1][j+1] += dp[i][j+1]
            dp[i+1][j+1] %= p
        if grid[i+1][j] == ".":
            dp[i+1][j+1] += dp[i+1][j]
            dp[i+1][j+1] %= p
print(dp[h][w])