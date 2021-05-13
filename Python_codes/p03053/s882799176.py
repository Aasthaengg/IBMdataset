import sys
from collections import deque
H,W = map(int,sys.stdin.readline().rstrip().split())
map = [[i for i in map(str,sys.stdin.readline().rstrip())] for _ in range(H)]
dist = [[-1]*W for _ in range(H)]
q = deque()
for i in range(H):
  for j in range(W):
    if map[i][j] == '#':
      q.append((i,j))
      dist[i][j] = 0

def bfs():
  while q:
    x,y = q.popleft()
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < H and 0 <= ny < W and map[nx][ny] == '.' and dist[nx][ny] == -1:
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
bfs()
ans = 0
for i in range(H):
  ans = max(max(dist[i][:]),ans)
print(ans)