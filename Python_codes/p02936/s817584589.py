from collections import deque
n,q=map(int,input().split())
G=[[] for _ in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
count=[0]*n
for i in range(q):
  p,x=map(int,input().split())
  count[p-1]+=x
stack=deque([0])
ans=[0]*n
ans[0]=count[0]
flag=[False]*n
while stack:
  v=stack.pop()
  flag[v]=True
  for nv in G[v]:
    if not flag[nv]:
      stack.append(nv)
      ans[nv]=ans[v]+count[nv]
print(*ans)