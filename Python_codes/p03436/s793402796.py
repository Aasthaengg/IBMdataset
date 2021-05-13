import sys 
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
H, W = map(int,readline().split())
grid = ['#']*(W+2)
for _ in range(H):
  grid += ['#'] + list(map(str,readline().decode().rstrip())) + ['X']
grid += ['#']*(W+2)
 
dist = [-1]*((H+2)*(W+2)-1)
 
s = W + 3
g = (H+1)*(W+2)-2
 
def bfs():
  while q:
    x = q.popleft()
    if x == g:
      return
    for dx in (1,W+2,-1,-W-2):
      if dist[x+dx] == -1 and grid[x+dx] =='.':
        dist[x+dx] = dist[x]+1
        q.append(x+dx)

dist[s]=0
q = deque([(s)])
bfs()

if dist[g] ==-1:
  print(-1)
else:
  print(grid.count('.')-dist[g]-1)