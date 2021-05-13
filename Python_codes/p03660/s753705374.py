import collections
import sys
sys.setrecursionlimit(10**9)

def dfs(v):
  ret=0
  for u in g[v]:
    if checked[u]==0:
      checked[u]=1
      ret+=1+dfs(u)
  return ret

n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
  u,v=map(int,input().split())
  g[u].append(v)
  g[v].append(u)
q=collections.deque()
pn=[-1]*(n+1)
checked=[0]*(n+1)
checked[1]=1
q.append(1)
cnt=0
while cnt!=n-1:
  v=q.popleft()
  for u in g[v]:
    if checked[u]==0:
      cnt+=1
      checked[u]=1
      q.append(u)
      pn[u]=v
path=[n]
while 1:
  tmp=pn[path[-1]]
  if tmp==1:
    break
  path.append(tmp)
path=path[::-1]
l=len(path)
if l==1:
  fg=n
  sg=1
else:
  fg=path[l//2]
  sg=path[l//2-1]
checked=[0]*(n+1)
checked[1]=1
checked[fg]=1
ans1=dfs(1)
ans2=(n-2)-ans1
if ans1>ans2:
  print('Fennec')
else:
  print('Snuke')