from collections import deque

h,w = map(int, input().split())
s = ["0" * (w+2)]  + ["0"+input()+"0" for i in range(h)] + ["0" * (w+2)] 
not_visited = [[0] * (w+2)] + [[0] + [1] * w + [0] for i in range(h)] + [[0] * (w+2)]
ans = 0
for i in range(1,h+1):
  for j in range(1,w+1):
    if s[i][j] == ".":
      continue
    black, white = 1,0
    queue = deque([(i,j,1)])
    not_visited[i][j] = 0
    while queue:
      H,W,color = queue.popleft()
      if not_visited[H-1][W]:
        if color and s[H-1][W] == ".":
          not_visited[H-1][W] = 0
          white += 1
          queue.append((H-1,W,0))
        elif color == 0 and s[H-1][W] == "#":
          not_visited[H-1][W] = 0
          black += 1
          queue.append((H-1,W,1))
      if not_visited[H+1][W]:
        if color and s[H+1][W] == ".":
          not_visited[H+1][W] = 0
          white += 1
          queue.append((H+1,W,0))
        elif color == 0 and s[H+1][W] == "#":
          not_visited[H+1][W] = 0
          black += 1
          queue.append((H+1,W,1))
      if not_visited[H][W-1]:
        if color and s[H][W-1] == ".":
          not_visited[H][W-1] = 0
          white += 1
          queue.append((H,W-1,0))
        elif color == 0 and s[H][W-1] == "#":
          not_visited[H][W-1] = 0
          black += 1
          queue.append((H,W-1,1))
      if not_visited[H][W+1]:
        if color and s[H][W+1] == ".":
          not_visited[H][W+1] = 0
          white += 1
          queue.append((H,W+1,0))
        elif color == 0 and s[H][W+1] == "#":
          not_visited[H][W+1] = 0
          black += 1
          queue.append((H,W+1,1))
    ans += black * white
print(ans)