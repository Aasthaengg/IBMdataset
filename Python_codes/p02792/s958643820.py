n = int(input())

mat = [[0]*10 for i in range(10)]

for i in range(n+1):
  if i % 10 != 0:
    str_i = str(i)
    mat[int(str_i[0])][int(str_i[-1])] += 1
c = 0
for y in range(1, 10):
  for x in range(y, 10):
    if y == x:
      c += mat[y][x] * mat[x][y]
    else:
      c += mat[y][x] * mat[x][y] * 2
print(c)
