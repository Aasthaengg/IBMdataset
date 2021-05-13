H, W = map(int, input().split())
S = []
D = [[-1, 0], [0, -1], [1, 0], [0, 1]]
for i in range(H):
  S.append(input())
f = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == "#":
      g = 0
      for k in range(4):
        if 0 <= i + D[k][0] < H and 0 <= j + D[k][1] < W and S[i+D[k][0]][j+D[k][1]] == "#":
          g = 1
      if g == 0:
        f = 1
if f == 0:
  print("Yes")
else:
  print("No")