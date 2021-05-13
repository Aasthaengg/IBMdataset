from collections import deque

H, W = map(int, input().split())
grid = []
for _ in range(H):
  grid.append(input())

def get_adj(pos):
  ans = []
  for v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    adj = (pos[0] + v[0], pos[1] + v[1])
    if adj[0] >= 0 and adj[0] < H and adj[1] >= 0 and adj[1] < W:
      ans.append(adj)
  return ans

start = (0, 0)
goal = (H-1, W-1)

q = deque()
q.append((start, 1))
visited = {}

while q:
  pos, dist = q.popleft()
  if grid[pos[0]][pos[1]] == '#':
    continue
  if pos in visited:
    continue
  visited[pos] = dist
  if pos == goal:
    break
  for adj in get_adj(pos):
    q.append((adj, dist+1))

cnt_walls = sum([row.count('#') for row in grid])

if goal in visited:
  print(H*W-visited[goal]-cnt_walls)
else:
  print(-1)