from collections import deque

mod = 10**9+7

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

cnt = [[0]*w for _ in range(h)]
cnt[0][0] = 1

D = deque()
D.append((0, 0))

dxdy = [(0, 1), (1, 0)]

appended =  [[False]*w for _ in range(h)]
appended[0][0] = True
while D:
  p = D.popleft()
  if p == (h-1, w-1):
    break
  for k in range(2):
    nx = p[0] + dxdy[k][0]
    ny = p[1] + dxdy[k][1]
    if 0<=nx<h and 0<=ny<w and maze[nx][ny]==".":
      cnt[nx][ny] += cnt[p[0]][p[1]]
      cnt[nx][ny] %= mod
      if appended[nx][ny]==False:
        D.append((nx, ny))
        appended[nx][ny] = True

print(cnt[h-1][w-1])