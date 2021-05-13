H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = []
for i in range(H):
  for j in range(W):
    if i == H-1 and j == W-1:
      continue
    if i == H-1:
      if A[i][j] % 2 == 1:
        A[i][j] -= 1; A[i][j+1] += 1;
        ans.append((i,j,i,j+1))
    elif A[i][j] % 2 == 1:
      A[i][j] -= 1; A[i+1][j] += 1;
      ans.append((i,j,i+1,j))
print(len(ans))
for i1, j1, i2, j2 in ans:
  print(i1+1, j1+1, i2+1, j2+1)