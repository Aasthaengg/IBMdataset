import sys
sys.setrecursionlimit(500000)
 
N,Q = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
  a,b = map(int,input().split())
  a-=1;b-=1 #頂点を0indexに
  G[a].append(b);G[b].append(a)
query = {}
for i in range(Q):
  p,x = map(int,input().split())
  p-=1
  if p not in query:
    query[p] = x
  else:
    query[p] += x
ans = [0 for _ in range(N)]
def dfs(v,par): #vが今いる頂点、parが親。
  if v in query:
    ans[v] += query[v]
  for u in G[v]:
    if u != par:
      ans[u] += ans[v]
      dfs(u,v)
dfs(0,-1)
print(*ans)