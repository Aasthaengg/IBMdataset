import sys
sys.setrecursionlimit(10**6)
f=lambda:map(int,input().split())
n,k=f()
g=[[] for _ in range(n)]
for i in range(n-1):
  a,b=f()
  g[a-1]+=[b-1]
  g[b-1]+=[a-1]
l=[0]*n
for _ in range(k):
  p,x=f()
  l[p-1]+=x
def dfs(v,p=-1):
  for c in g[v]:
    if c==p: continue
    l[c]+=l[v]
    dfs(c,v)
dfs(0)
print(*l)