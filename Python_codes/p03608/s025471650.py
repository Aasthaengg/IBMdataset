n, m, r = map(int, input().split())
rs = list(map(int, input().split()))
rs = [i-1 for i in rs]
d = [[float('inf')] * n for i in range(n)]
for i in range(m):
    x, y, r = map(int, input().split())
    x -= 1
    y -= 1
    d[x][y] = r
    d[y][x] = r

for i in range(n):
    d[i][i] = 0

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

d = warshall_floyd(d)

ans = float('inf')
from itertools import permutations
for i in permutations(rs):
    di = 0
    for j in range(len(rs) - 1):
        di += d[i[j]][i[j + 1]]
    ans = min(ans, di) 

print(ans)