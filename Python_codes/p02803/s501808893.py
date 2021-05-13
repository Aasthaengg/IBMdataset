from collections import deque
def bfs(maze,sy,sx):
  queue=deque([[sy,sx]])
  visited=[[0]*w for _ in range(h)]
  visited[sy][sx]=1
  mx=0
  while queue:
    y,x=queue.popleft()
    for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
      n_y,n_x=y+j,x+k
      if not (0<=n_y<h and 0<=n_x<w):
        continue
      if maze[n_y][n_x]=='.' and visited[n_y][n_x]==0:
        visited[n_y][n_x]=visited[y][x]+1
        mx=max(mx,visited[n_y][n_x])
        queue.append([n_y,n_x])
  return mx

h,w=map(int,input().split())
s=[input() for _ in range(h)]
ans=0
for sy in range(h):
  for sx in range(w):
    if s[sy][sx]=='#':
      continue
    ans=max(ans,bfs(s,sy,sx)-1)
print(ans)