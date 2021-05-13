from collections import deque

H, W = map(int,input().split())
maze = list(list(input()) for i in range(H))



def bfs(maze,maze_s,sy,sx):
  maze_s[sy][sx] = 0
  queue = deque([[sy,sx]])
  while queue:
    y,x = queue.popleft()
    if maze[y][x] == "g":
      return maze_s[y][x]
    else:
      for j,k in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_y,new_x = y+j, x+k
        if 0 <= new_y <= H-1 and 0 <= new_x <= W-1:
          if maze[new_y][new_x] != "#" and maze_s[new_y][new_x] == -1:
            maze_s[new_y][new_x] = maze_s[y][x] + 1
            queue.append([new_y,new_x])
  else:
    print(-1)
    exit()

maze_s = list([-1] * W for i in range(H))
count = 0
for row in maze:
  count += row.count(".")

maze[H-1][W-1] = "g"

ans = count - bfs(maze,maze_s,0,0) -1
print(ans)