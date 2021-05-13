from collections import deque

H, W = map(int, input().split())

maze = "#" * (W+2)
for _ in range(H):
  maze += "#" + input() + "#"
maze += "#" * (W+2)

dist = [-1] * (W+2) * (H+2)
q = deque()

dist[(W+2) * 1 + 1] = 0
q.append((W+2) * 1 + 1)

while len(q) != 0:
  v = q.popleft()
  
  udlr = (-W-2, W+2, -1, 1)
  for move in udlr:
    nv = v + move
    if maze[nv] == "#":
      continue
    if dist[nv] != -1:
      continue
    dist[nv] = dist[v] + 1
    q.append(nv)
if dist[(W+2) * H + W] == -1:
  print(-1)
else:
  print(W * H - maze.count("#") + 2 * (W + H + 2) - dist[(W+2) * H + W] -1)