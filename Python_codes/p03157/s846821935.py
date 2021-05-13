from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
  stack = deque()
  stack.append((x, y))
  num_w = 0
  num_b = 0
  while stack:
    cx, cy = stack.popleft()
    cc = S[cy][cx]
    for i, j in zip(dx, dy):
      nx = i + cx
      ny = j + cy
      if (0 <= nx < w and 0 <= ny < h) and not visited[ny][nx] and S[ny][nx] != cc:
        visited[ny][nx] = True
        stack.append((nx, ny))
        if cc == ".":
          num_w += 1
        else:
          num_b += 1
  else:
    return num_w, num_b

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

visited = [[False] * w for _ in range(h)]
  
ans = 0
for i in range(w):
  for j in range(h):
    if not visited[j][i]:
      num_w, num_b = dfs(i, j)
      ans += num_b * num_w
      
print(ans)