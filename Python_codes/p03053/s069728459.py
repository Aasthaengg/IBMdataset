from collections import deque

H, W = map(int, input().split())
mp = [list(input()) for _ in range(H)]

ds = [[-1,0],[1,0],[0,-1],[0,1]]
q = deque([])

cnt = 0

for i in range(H):
  for j in range(W):
    if mp[i][j] == '#':
      q.append((i,j,0))
      cnt += 1

if cnt == H*W:
  print(0)
  exit()

while q:
  t = q.popleft()
  for d in ds:
    ny = t[0]+d[0]
    nx = t[1]+d[1]
    if 0 <= ny < H and 0<= nx < W:
      if mp[ny][nx] == '.':
        mp[ny][nx] = '#'
        q.append((ny,nx,t[2]+1))
        cnt += 1
        if cnt == H*W:
          print(t[2]+1)
          exit()
