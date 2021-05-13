def WarshallFloyd(d):
    v = len(mat)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

n,m,r = map(int, input().split())
ls = list(map(int, input().split()))
INF = 1001001001001
mat = [[INF]*n for _ in range(n)]
for i in range(m):
    u,v,c = map(int, input().split())
    u-=1
    v-=1
    mat[u][v]=c
    mat[v][u]=c

WarshallFloyd(mat)

from itertools import permutations

ans=INF
for p in permutations(ls):
    now=0
    for i in range(len(p)-1):
        now+=mat[p[i]-1][p[i+1]-1]
    ans=min(ans,now)

print(ans)




