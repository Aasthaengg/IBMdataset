from itertools import permutations as perm
n, m, r = map(int, input().split())
rs = list(map(int, input().split()))
grid = [[float('inf')]*n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    grid[a-1][b-1] = c
    grid[b-1][a-1] = c
for i in range(n):
    for j in range(n):
        if i == j:
            grid[i][j] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

perms = rs
res = float('inf')
for p in perm(perms):
    tmp = 0
    for i in range(1,r):
        tmp += grid[p[i]-1][p[i-1]-1]
    res = min(res,tmp)
print(res)