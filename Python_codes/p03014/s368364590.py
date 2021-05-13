H,W = map(int,input().split())

s = []
l = [[0] * W for i in range(H)]
r = [[0] * W for i in range(H)]
u = [[0] * W for i in range(H)]
d= [[0] * W for i in range(H)]
  
for i in range(H):
    tmp =list(input())
    s.append(tmp)

for y in range(H):
  for x in range(W):
    if s[y][x] == "#":
      continue
    elif x == 0:
      l[y][x] = 1
    else:
      l[y][x] = l[y][x-1] + 1

for y in range(H):
  for x in range(W-1, -1, -1):
    if s[y][x] == "#":
      continue
    elif x == W - 1:
      r[y][x] = 1
    else:
      r[y][x] = r[y][x+1] + 1
      
for y in range(H):
  for x in range(W):
    if s[y][x] == "#":
      continue
    elif y == 0:
      u[y][x] = 1
    else:
      u[y][x] = u[y-1][x] + 1
      
for y in range(H-1, -1, -1):
  for x in range(W):
    if s[y][x] == "#":
      continue
    elif y == H - 1:
      d[y][x] = 1
    else:
      d[y][x] = d[y+1][x] + 1

ans = 0
for x in range(H):
  for y in range(W):
    if ans < l[x][y] + r[x][y] + u[x][y] + d[x][y] - 3:
      ans = l[x][y] + r[x][y] + u[x][y] + d[x][y] - 3
      
print(ans)