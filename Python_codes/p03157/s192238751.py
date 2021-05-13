from collections import deque
h,w = (int(i) for i in input().split())
maze = [input() for _ in range(h)]
visited = [[False]*w for _ in range(h)]
  
def solve2(i,j):
  d = [(1,0),(0,1),(-1,0),(0,-1)]
  queue = deque([(i,j)])
  b,c = 0,0
  while queue:
    (x,y) = queue.popleft()
    if maze[x][y] =='#':b+=1
    else:c += 1
    visited[x][y] = True
    
    for dx,dy in d:
      nx,ny = x+dx,y+dy
      #print(nx,ny)
      if nx <= -1 or nx >= h or ny <= -1 or ny >= w:
        continue
      if visited[nx][ny]:
        continue
      #print(maze[nx][ny],maze[x][y])
      if maze[nx][ny] != maze[x][y]:
       visited[nx][ny] = True
       queue.append([nx,ny])
        
 # print(b,c)
  return b*c

ans = 0
for i in range(h):
  for j in range(w):
    if not visited[i][j]:
     ans += solve2(i,j)
print(ans)