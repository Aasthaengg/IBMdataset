from collections import deque

row, col = map(int, input().split())
graph = [list(input()) for i in range(row)]

ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

seen = deque([])
finished = deque([])

for i in range(row):
  for j in range(col):
    if graph[i][j] == "#":
      finished.append([i, j])
      
while True:

  while len(finished) > 0:
    v = finished.popleft()
    for j in range(4):
      next_y, next_x = v[0]+dy[j], v[1]+dx[j]
      if not 0 <= next_y < row or not 0 <= next_x < col:
        continue
      if graph[next_y][next_x] == '#':
        continue 

      graph[next_y][next_x] = "#"
      seen.append([next_y, next_x])
  
  if len(seen) == 0:
    break
  seen, finished = deque([]), seen
  ans += 1
      
print(ans)