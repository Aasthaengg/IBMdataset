H,W = map(int,input().split())
maze = []
for i in range(H):
  s = input()
  maze.append(s)
def distance(maze,H,W):
  wall = []
  for i in range(H):
    w = [-1]
    for j in range(W):
      if maze[i][j] == '#':
        w.append(j)
    w.append(W)
    wall.append(w)

  wd = [[0]*W for _ in range(H)]
  for i in range(H):
    w1 = 0
    for j in range(W):
      if maze[i][j] == '#':
        w1 = min(w1+1,len(wall[i])-1)
        continue
      wd[i][j] = j-wall[i][w1]-1+wall[i][w1+1]-j-1

  return wd

wd = distance(maze,H,W)
maze = [list(x) for x in zip(*maze)]
hd = distance(maze,W,H)
max_dist = 1

for i in range(H):
  for j in range(W):
    max_dist = max(max_dist,wd[i][j] + hd[j][i]+1)
print(max_dist)