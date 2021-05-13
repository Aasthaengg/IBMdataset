# D - People on a Line
import sys
sys.setrecursionlimit(10 ** 9)

n,m = map(int,input().split())
e = [[] for _ in range(n)]
for i in range(m):
  l,r,d = map(int,input().split())
  l -= 1
  r -= 1
  e[l].append((r,d))
  e[r].append((l,-d))

INF = float('inf')
c = [INF for _ in range(n)]

def dfs(u,x):
  c[u] = x
  for v,d in e[u]:
    if c[v] != INF:
      if c[v] == c[u]+d:
        continue
      else:
        print('No')
        exit()
    else:
      dfs(v,c[u]+d)

for i in range(n):
  if c[i] == INF:
    dfs(i,0)
print('Yes')
