from collections import deque
n,m=map(int,input().split())
l=[[] for _ in range(n)]
edge=[]
ans=0
for _ in range(m):
  a,b=map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)
  edge.append([a-1,b-1])
for i,j in edge:
  q=deque([i])
  visited=[0]*n
  while q:
    x=q.pop()
    if x==j:
      break
    visited[x]=1
    for k in l[x]:
      if visited[k]==0 and not (x==i and k==j):
        q.append(k)
  else:
    ans+=1
print(ans)