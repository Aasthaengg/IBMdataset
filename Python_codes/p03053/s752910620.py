from collections import deque

H,W = map(int,input().split())
maze = list(list(input()) for i in range(H))
maze_s = [[-1] * W for i in range(H)]
queue = deque([])
for i,row in enumerate(maze):
  for j,value in enumerate(row):
    if value == "#":
      queue.append([i, j])
      maze_s[i][j] = 0
def bfs(maze, maze_s):
  while queue:
    y,x = queue.popleft()
    for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
      new_y,new_x= y+i,x+j
      if 0 <= new_y <= H-1 and 0<= new_x <= W-1:
        if maze[new_y][new_x] == "." and maze_s[new_y][new_x] == -1:
          maze_s[new_y][new_x] = maze_s[y][x] + 1
          queue.append([new_y,new_x])
  c = 0
  for row in maze_s:
    m = max(row)
    c = max(c,m)
  print(c)

bfs(maze,maze_s)