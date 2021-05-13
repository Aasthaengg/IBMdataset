from collections import deque

h,w=map(int,input().split())

maze=[list(input()) for i in range(h)]


dx=[1,-1,0,0]
dy=[0,0,1,-1]

Q=deque()

for i in range(h):
  for j in range(w):
    if maze[i][j]=='#':
      Q.append((i,j,0))


while Q:
  x,y,z=Q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if 0<=nx<h and 0<=ny<w and maze[nx][ny]=='.':
      Q.append((nx,ny,z+1))
      maze[nx][ny]='#'


print(z)
