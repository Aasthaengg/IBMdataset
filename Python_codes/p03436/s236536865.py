from collections import deque
H,W = map(int,input().split())
l = [str(input()) for _ in range(H)]
white_count = 0
for s in l:
  white_count += s.count('.')
sy = 0
sx = 0
gy = H-1
gx = W-1
visited = [[-1]*W for _ in range(H)]
visited[sy][sx] = 0
Q = deque([[sy,sx]])
while Q:
  y,x = Q.popleft()
  if [y,x] == [gy,gx]:
    print(white_count - visited[y][x] - 1)
    exit()
  for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
    if 0 <= x+j < W and 0 <= y+i < H and visited[y+i][x+j] == -1 and l[y+i][x+j] == '.':
      visited[y+i][x+j] = visited[y][x]+1
      Q.append([y+i,x+j])
    else:
      continue
print(-1)