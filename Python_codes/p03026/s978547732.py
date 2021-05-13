import sys
import resource

sys.setrecursionlimit(20000)
n=int(input())
edges=[list(map(int,input().split())) for i in range(n-1)]
e = [[] for i in range(n)]
for a,b in edges:
  a-=1;b-=1
  e[a].append(b);e[b].append(a)
c=sorted(list(map(int,input().split())))
print(sum(c[:-1]))
visited=[False for i in range(n)]
node=[0]*n
cnt=0
def dfs(pos):
  global cnt,node,c
  if visited[pos]:return
  visited[pos]=True
  for p in e[pos]:
    dfs(p)
  node[pos]=c[cnt]
  cnt+=1
dfs(0)
print(' '.join(map(str,node)))