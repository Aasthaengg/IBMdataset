from itertools import permutations
n,m,R = map(int,input().split())
r = [int(i)-1 for i in input().split()]
INF = float("INF")
d = [[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
ans = INF
for p in permutations(r):
    res = 0
    for i in range(R-1):
        res += d[p[i]][p[i+1]]
    ans = min(ans, res)
print(ans)