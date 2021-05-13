H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == "#":
      flag = 0
      if i > 0 and S[i-1][j] == "#":
        flag = 1
      if i < H-1 and S[i+1][j] == "#":
        flag = 1
      if j > 0 and S[i][j-1] == "#":
        flag = 1
      if j < W-1 and S[i][j+1] == "#":
        flag = 1
      if flag == 0:
        ans = 1
print("Yes" if ans == 0 else "No")