h,w = map(int,input().split())

grid = []

for i in range(h):
    grid.append(input())

dp = [[0 for i in range(w)] for i in range(h)]

dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if grid[i][j] != "#":
            if i-1 >= 0:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0:
                dp[i][j] += dp[i][j-1]
mod = 1000000007
print(dp[-1][-1] % mod)