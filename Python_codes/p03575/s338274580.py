from collections import deque
from copy import deepcopy

n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]

def DFS(m):
  t_l=deepcopy(l)
  del t_l[m]

  tree=[[] for j in range(n)]
  for a,b in t_l:
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)

  seen=set()
  seen.add(0)

  dq=deque()
  dq.append(0)

  while dq:
    x=dq.pop()
    for i in tree[x]:
      if i not in seen:
        dq.append(i)
        seen.add(i)

  return seen

ans=0
for i in range(m):
  st=DFS(i)
  if len(st)!=n:
    ans+=1

print(ans)