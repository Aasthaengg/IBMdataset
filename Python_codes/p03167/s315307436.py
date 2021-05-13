h, w = map(int, input().split())

grid = []
for _ in range(h):
    temp = list(input())
    grid.append(temp)


dp = [[0 for i in range(w)] for j in range(h)]
dp[0][0] = 1
MOD = 10**9 + 7

for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            if i > 0:
                dp[i][j] += dp[i-1][j] % MOD
            if j > 0:
                dp[i][j] += dp[i][j-1] % MOD

print(dp[-1][-1] % MOD)