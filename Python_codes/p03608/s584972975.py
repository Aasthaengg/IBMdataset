def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n, m, r = map(int,input().split()) #n:頂点数　m:辺の数 r:訪れる町の数
R = list(map(int,input().split()))

d = [[float("inf") for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(m):
    x, y, z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
wa = warshall_floyd(d)

# 訪れる町の順番を順列で用意
from itertools import permutations
ptn = permutations(R)

ans = 10**19
for p in ptn:
  cost = 0
  roots = [(j-1, i-1) for i, j in zip(p, p[1:])]
  for i, j in roots:
    cost += wa[i][j]
  ans = min(ans, cost)
  
print(ans)