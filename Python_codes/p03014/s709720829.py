H, W = [int(i) for i in input().split()]
M = []
for i in range(H):
  S = input()
  M.append(S)

X = []
for i in range(H):
  C = [0 for _ in range(W)]
  count = 0
  for j in range(W-1, -1, -1):
    if M[i][j] == ".":
      count += 1
      C[j] = count
    else:
      count = 0

  r = [0 for _ in range(W)]
  current = C[0]
  for j in range(W):
    if M[i][j] == ".":
      r[j] = current
    else:
      r[j] = 0
      if j + 1 < W:
        current = C[j+1]
  X.append(r)
Y = []
for i in range(W):
  C = [0 for _ in range(H)]
  count = 0
  for j in range(H-1, -1, -1):
    if M[j][i] == ".":
      count += 1
      C[j] = count
    else:
      count = 0

  r = [0 for _ in range(H)]
  current = C[0]
  for j in range(H):
    if M[j][i] == ".":
      r[j] = current
    else:
      r[j] = 0
      if j + 1 < H:
        current = C[j+1]
  Y.append(r)

ans = 0
for i in range(H):
  for j in range(W):
    ans = max(ans, X[i][j]+Y[j][i]-1)
print(ans)
