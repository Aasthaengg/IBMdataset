h, w = map(int, input().split()) 
map = []
for _ in range(h):
  map.append(list(input()))

r = [[0] * w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if map[i][j] == ".":
      if j == 0:
        r[i][j] = 1
      else:
        r[i][j] = r[i][j-1] + 1

l = [[0] * w for _ in range(h)]
for i in range(h):
  for j in range(w-1, -1, -1):
    if map[i][j] == ".":
      if j == w - 1:
        l[i][j] = 1
      else:
        l[i][j] = l[i][j+1] + 1
        
d = [[0] * w for _ in range(h)]
for i in range(w):
  for j in range(h):
    if map[j][i] == ".":
      if j == 0:
        d[j][i] = 1
      else:
        d[j][i] = d[j-1][i] + 1

u = [[0] * w for _ in range(h)]
for i in range(w):
  for j in range(h-1, -1, -1):
    if map[j][i] == ".":
      if j == h-1:
        u[j][i] = 1
      else:
        u[j][i] = u[j+1][i] + 1
ans = 0
for i in range(h):
  for j in range(w):
    num = l[i][j] + r[i][j] + d[i][j] + u[i][j] - 3
    if num > ans:
      ans = num
print(ans)
