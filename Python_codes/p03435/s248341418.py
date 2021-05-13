c = [list(map(int, input().split())) for _ in range(3)]
flag = True
for i in range(3):
  x = [0]*3
  y = [0]*3
  for j in range(3):
    x[j] = c[i-1][j] - c[i][j]
    y[j] = c[j][i-1] - c[j][i]
  if len(set(x)) != 1 or len(set(y)) != 1:
    flag = False
if flag:
  print("Yes")
else:
  print("No")