h, w = map(int, input().split())
mat = []
for i in range(h):
  mat.append(list(map(int, input().split())))
sousa = []
for y in range(h):
  if y % 2 == 0:
    x = -1
    for x in range(w-1):
      if mat[y][x] % 2 == 1:
        mat[y][x] -= 1
        mat[y][x+1] += 1
        sousa.append((y+1, x+1, y+1, x+1+1))
    x += 1
    if mat[y][x] % 2 == 1 and y < h-1:
        mat[y][x] -= 1
        mat[y+1][x] += 1
        sousa.append((y+1, x+1, y+1+1, x+1))
  if y % 2 == 1:
    x = w
    for x in range(w-1, 0, -1):
      if mat[y][x] % 2 == 1:
        mat[y][x] -= 1
        mat[y][x-1] += 1
        sousa.append((y+1, x+1, y+1, x+1-1))
    x -= 1
    if mat[y][x] % 2 == 1 and y < h-1:
        mat[y][x] -= 1
        mat[y+1][x] += 1
        sousa.append((y+1, x+1, y+1+1, x+1))

print(len(sousa))
for y,x,y1,x1 in sousa:
  print(y,x,y1,x1)
