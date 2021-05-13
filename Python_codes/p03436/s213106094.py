from collections import deque
H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]

s = (0,0)
g = (H-1,W-1)

ans = 0
task = deque([(s,0)])
visited = [[0 for _ in range(W)] for _ in range(H)]
visited[s[0]][s[1]] = 1
flag = False
while task:
  p, c = task.popleft()
  x = p[0]
  y = p[1]
  if p == g:
    ans = c
    flag = True
    break 
  if x >= 1 and visited[x-1][y] == 0 and M[x-1][y] == ".":
    visited[x-1][y] = 1
    task.append(((x-1,y),c+1))
  if y >= 1 and visited[x][y-1] == 0 and M[x][y-1] == ".":
    visited[x][y-1] = 1
    task.append(((x,y-1),c+1))
  if x <= H-2 and visited[x+1][y] == 0 and M[x+1][y] == ".":
    visited[x+1][y] = 1
    task.append(((x+1,y),c+1))
  if y <= W-2 and visited[x][y+1] == 0 and M[x][y+1] == ".":
    visited[x][y+1] = 1
    task.append(((x,y+1),c+1))     

point = H*W -sum([M[i].count("#") for i in range(H)]) - ans -1
print(point if flag else -1)