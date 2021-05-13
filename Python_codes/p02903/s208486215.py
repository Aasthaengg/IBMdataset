H, W, A, B = map(int, input().split())
L = [[0 for __ in range(W)] for _ in range(H)]
for i in range(B):
  for j in range(A):
    L[i][j] = 1
for i in range(B, H):
  for j in range(A, W):
    L[i][j] = 1
for i in range(H):
  for j in range(W):
    print(L[i][j], end = '')
  print()