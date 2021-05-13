import collections
import sys
sys.setrecursionlimit(10**7)

def dfs(u):
  for v in g[u]:
    if checked[v]==1:
      continue
    else:
      checked[v]=1
      depth2[u]=max(depth2[u],dfs(v)+1)
  return depth2[u]

n,u,v=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  g[a].append(b)
  g[b].append(a)
depth=[0]*(n+1)
checked=[0]*(n+1)
checked[v]=1
q=collections.deque()
q.append((v,0))
while 1:
  if len(q)==0:
    break
  tu,d=q.popleft()
  checked[tu]=1
  depth[tu]=d
  for tv in g[tu]:
    if checked[tv]!=1:
      checked[tv]=1
      q.append((tv,d+1))
moves=(depth[u]-1)//2
depth2=[0]*(n+1)
checked=[0]*(n+1)
checked[v]=1
dfs(v)
checked=[0]*(n+1)
checked[u]=1
q=collections.deque()
q.append((u,0))
cand=[]
while 1:
  if len(q)==0:
    break
  tu,d=q.popleft()
  if d==moves:
    cand.append(tu)
  checked[tu]=1
  for tv in g[tu]:
    if checked[tv]!=1:
      checked[tv]=1
      q.append((tv,d+1))
md=0
for i in cand:
  md=max(md,depth2[i])
if depth[u]%2!=0:
  ans=moves+md
else:
  ans=moves+md+1
print(ans)