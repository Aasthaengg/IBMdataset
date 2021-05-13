H, W = map(int, input().split())
data = []
for i in range(H):
  data.append(input())
x = [1,1,1,0,-1,-1,-1,0]
y = [1,0,-1,-1,-1,0,1,1]
ans = []
for i in range(H):
  s = ""
  for j in range(W):
    if data[i][j] == "#":
      s += "#"
      continue
    else:
      count = 0
      for k in range(8):
        if 0 <= i + x[k] and i + x[k] < H and 0 <= j + y[k] and j + y[k] < W:
          if data[i + x[k]][j + y[k]] == "#":
            count += 1
      count = str(count)
      s += count
  ans.append(s)
for i in range(H):
  print(ans[i])