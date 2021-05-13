def print_dp(dp):
    i_len = len(dp)
    j_len = len(dp[0])
    tmp_dp = [[0]*i_len for _ in range(j_len)]
    for i in range(i_len):
        for j in range(j_len):
            tmp_dp[j][i] = dp[i][j]
    for i in range(j_len):
        print(tmp_dp[i])

import copy
n = int(input())
grid = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    lis = list(map(int, input().split()))
    for j in range(n):
        if i == j:
            grid[i][j] = 0
        else:
            grid[i][j] = lis[j]
grid_m = copy.deepcopy(grid)

for k in range(n):
    for i in range(n):
        for j in range(n):
            grid[i][j] = min(grid[i][j],grid[i][k]+grid[k][j])

ok = True
for i in range(n):
    for j in range(n):
        if not grid[i][j] == grid_m[i][j]:
            ok = False
if not ok:
    print(-1)
else:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k or j == k:
                    continue
                if grid[i][j] == grid[i][k] + grid[k][j] and grid[i][k] != 0 and grid[k][j] != 0:
                    grid[i][j] = 0
    res = 0
    for i in range(n):
        res += sum(grid[i])
    print(res//2)