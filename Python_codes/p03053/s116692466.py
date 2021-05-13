from collections import deque

inf=float('inf')

h,w=map(int,input().split())
maze=[]
st=[]
for j in range(h):
  a=list(input())
  for i in range(w):
    if a[i]=='.':
      a[i]=inf
    if a[i]=='#':
      a[i]=0
      st.append([j,i])
  maze.append(a)
  
de=deque(st)

while de:
  v=de.popleft()
  sy,sx=v[0],v[1]
  for p in ([1,0],[0,1],[-1,0],[0,-1]):
    ny,nx=sy+p[0],sx+p[1]
    if 0<=ny<=h-1 and 0<=nx<=w-1 and maze[ny][nx]!=0:
      if maze[ny][nx]>maze[sy][sx]+1:
        maze[ny][nx]=maze[sy][sx]+1
        de.append([ny,nx])

ans=0
for g in range(h):
  for f in range(w):
    ans=max(maze[g][f],ans)

print(ans)