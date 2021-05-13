# D - Candidates of No Shortest Paths
# ワーシャルフロイド法で、任意の2頂点間の最短距離を求める。
# すべての辺に対して、その距離と、辺の両端間の最短距離を比較し、
# 辺の距離 > 辺の両端間の最短距離なら、その辺は最短経路に使われていないことがわかる。
n,m = map(int,input().split())
e = []
for i in range(m):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  e.append((a,b,c))

INF = float('inf')
d = [[INF for _ in range(n)] for _ in range(n)]
for a,b,c in e:
  d[a][b] = c
  d[b][a] = c
for i in range(n):
  d[i][i] = 0
for k in range(n):
  for i in range(n):
    for j in range(n):
      d[i][j] = min(d[i][k]+d[k][j],d[i][j])
ans = 0
for a,b,c in e:
  if d[a][b] < c:
    ans += 1
print(ans)