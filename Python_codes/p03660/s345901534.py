n=int(input())
ki=[[] for _ in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  ki[a-1].append(b-1)
  ki[b-1].append(a-1)
fe=[0]*n
sn=[0]*n
from collections import deque
d=deque()
d.append(0)
visited=[False]*n
visited[0]=True
while d:
  g=d.popleft()
  for i in ki[g]:
    if visited[i]:
      continue
    d.append(i)
    visited[i]=True
    fe[i]=fe[g]+1
d=deque()
d.append(n-1)
visited=[False]*n
visited[n-1]=True
while d:
  g=d.popleft()
  for i in ki[g]:
    if visited[i]:
      continue
    d.append(i)
    visited[i]=True
    sn[i]=sn[g]+1
x=0
for i in range(n):
  if fe[i]>sn[i]:
    x+=1
  else:
    x-=1
print('Fennec' if x<0 else 'Snuke')