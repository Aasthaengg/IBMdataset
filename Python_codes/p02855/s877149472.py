import numpy as np
H,W,K = map(int,input().split())
S = [list(str(input())) for _ in range(H)]

l = np.array([['0' for _ in range(W)]]*H)
l = l.tolist()
k= 1
for i in range(H):
  for j in range(W):
    if S[i][j] == '#':
      l[i][j] = str(k)
      k += 1
for i in range(H):
  for j in range(W):
    if l[i][j] == '0':
      if i > 0:
        l[i][j] = l[i-1][j]
      else:
        for m in range(1,H-i):
          if l[i+m][j] != '0':
            l[i][j] = l[i+m][j]
            break
for i in range(H):
  for j in range(W):
    if l[i][j] == '0':
      if j > 0:
        l[i][j] = l[i][j-1]
      else:
        for m in range(1,W-j):
          if l[i][j+m] != '0':
            l[i][j] = l[i][j+m]
            break
  print(' '.join(l[i]))