H, W = map(int, input().split())
A = []
for i in range(H):
  A.append(input())
dis = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for i in range(H):
  s = ""
  for j in range(W):
    if A[i][j] == "#":
      s += "#"
    else:
      count = 0
      for d in dis:
        if 0 <= i + d[0] < H and 0 <= j + d[1] < W:
          if A[i+d[0]][j+d[1]] == "#":
            count += 1
      s += str(count)
  print(s)