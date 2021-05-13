c = [list(map(int, input().split())) for _ in range(3)]

b = c[0]
a = [0, c[1][0] - b[0], c[2][0] - b[0]]

flag = True
for i in range(3):
  for j in range(3):
    if c[i][j] != a[i] + b[j]:
      flag = False
      
print("Yes" if flag else "No")