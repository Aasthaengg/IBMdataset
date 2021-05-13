H, W = map(int, input().split())
C = [input() for _ in range(H)]
ans = [[0]*W for _ in range(2*H)]

for i in range(2*H):
  for j in range(W):
    ans[i][j] = C[i//2][j]
  print(*ans[i], sep="")