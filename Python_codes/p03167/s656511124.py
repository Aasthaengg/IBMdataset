H,W = map(int, input().split())
M = 10**9 + 7
A = []
for _ in range(H):
  S = input()
  A.append(S)
L = [[0 for j in range(W)] for i in range(H)]
L[0][0] =  1
for i in range (H):
  for j in range (W):
    if A[i][j] == '.':
        if i > 0:
            L[i][j] += L[i-1][j] % M
        if j > 0:
            L[i][j] += L[i][j-1] % M
print(L[H-1][W-1] % M)