import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5+1)
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
for i in range(m):
  u,v,c=map(int,input().split())
  g[u-1].append((v-1,c))
  g[v-1].append((u-1,-c))
x=[None]*n
for i in range(n):
  if x[i]==None:
    x[i]=0
    dfs(i)
print('Yes')
