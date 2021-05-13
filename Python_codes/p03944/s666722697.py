W,H,N = map(int,input().split())

grid = []
for i in range(W):
  grid.append([])
  for j in range(H):
    grid[i].append(0)

for _ in range(N):
  x,y,a = map(int,input().split())
  if a == 1:
    for i in range(x):
      for j in range(H):
        grid[i][j] = 1
  elif a == 2:
    for i in range(x,W):
      for j in range(H):
        grid[i][j] = 1
  elif a == 3:
    for i in range(W):
      for j in range(y):
        grid[i][j] = 1
  else:
    for i in range(W):
      for j in range(y,H):
        grid[i][j] = 1
count = 0
for i in range(W):
  for j in range(H):
    count += 1 - grid[i][j]
print(count)