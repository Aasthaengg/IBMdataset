h, w, k = map(int, input().split())
L = [[0]*w for _ in range(h)]
now = 1
for i in range(h):
  s = input()
  for j in range(w):
    if s[j] == ".":
      L[i][j] = 0
    else:
      L[i][j] = now
      now += 1
for i in range(h):
  for j in range(w-1):
    if L[i][j+1] == 0:
      L[i][j+1] = L[i][j]
for i in range(h):
  for j in range(w-1):
    if L[i][w-2-j] == 0:
      L[i][w-2-j] = L[i][w-1-j]
for i in range(h-1):
  for j in range(w):
    if L[i+1][j] == 0:
      L[i+1][j] = L[i][j]
for i in range(h-1):
  for j in range(w):
    if L[h-2-i][j] == 0:
      L[h-2-i][j] = L[h-1-i][j]
for i in L:
  print(*i)