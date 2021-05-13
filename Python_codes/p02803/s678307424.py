h,w=map(int,input().split())

A=[]
for i in range(h):
  s=input()
  A.append([s[i] for i in range(w)])
g=[[[]for i in range(w)] for _ in range(h)]

for i in range(h):
  for j in range(w):
    if A[i][j]=='.':
      if i-1>=0:
          if A[i-1][j]=='.':
            g[i][j].append((i-1,j))
      if i+1<h:
          if A[i+1][j]=='.':
            g[i][j].append((i+1,j))          
      if j+1<w:
          if A[i][j+1]=='.':
            g[i][j].append((i,j+1))          
      if j-1>=0:
          if A[i][j-1]=='.':
            g[i][j].append((i,j-1))  
        
from collections import deque
def bfs(a,b):
  time=[[-1]*w for _ in range(h)]
  time[a][b]=0
  stack=deque([])
  stack.append((a,b))
  n=1
  while stack:
    d=stack.popleft()
    for v in g[d[0]][d[1]]:
      if time[v[0]][v[1]]==-1:
        time[v[0]][v[1]]=time[d[0]][d[1]]+1
        stack.append(v)
        
      else:
        continue
     
  timem=0
  for i in range(h):
    for j in range(w):
      timem=max(timem,time[i][j])
  return timem
ans=0
for i in range(h):
  for j in range(w):
    bfsm=bfs(i,j)
    ans=max(ans,bfsm)
print(ans)