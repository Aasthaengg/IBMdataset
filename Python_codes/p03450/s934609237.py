import sys
sys.setrecursionlimit(10**7)
def dfs(p):
  for edge in g[p]:
    if x[edge[0]] is not None:
      if x[edge[0]]-x[p]!=edge[1]:
        print('No')
        exit()
    else:
      x[edge[0]]=x[p]+edge[1]
      dfs(edge[0])
n,m=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(m):
  l,r,d=map(int,input().split())
  g[r-1].append((l-1,d))
  g[l-1].append((r-1,-d))
x=[None]*n
for i in range(n):
  if x[i]==None:
    x[i]=0
    dfs(i)
print('Yes')