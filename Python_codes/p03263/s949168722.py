H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
cnt = 0
ans = []
for i in range(H):
  for j in range(W):
    if i == H-1 and j == W-1:
      continue
    if i == H-1:
      if A[i][j] % 2 == 1:
        A[i][j] -= 1; A[i][j+1] += 1;
        s = " ".join([str(i+1), str(j+1), str(i+1), str(j+2)])
        ans.append(s)
        cnt += 1
    elif A[i][j] % 2 == 1:
      A[i][j] -= 1; A[i+1][j] += 1;
      s = " ".join([str(i+1), str(j+1), str(i+2), str(j+1)])
      ans.append(s)
      cnt += 1
print(cnt)
print(*ans, sep="\n")