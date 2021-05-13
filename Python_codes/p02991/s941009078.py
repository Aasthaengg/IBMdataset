n,m=map(int,input().split())
g=[[] for _ in range(n)]
gg=[[] for _ in range(3*n)]
for _ in range(m):
  a,b=map(int,input().split())
  a,b=a-1,b-1
  gg[a].append(n+b)
  gg[n+a].append(2*n+b)
  gg[2*n+a].append(b)
s,t=map(int,input().split())
s,t=s-1,t-1
from collections import deque
todo=deque([s])
seen=[-1]*(3*n)
seen[s]=0
while todo:
  v=todo.popleft()
  for l in gg[v]:
    if seen[l]==-1:
      todo.append(l)
      seen[l]=seen[v]+1
      if l==t:
        print(seen[l]//3)
        exit()
if seen[t]>0:
  print(seen[t]//3)
else:
  print(-1)