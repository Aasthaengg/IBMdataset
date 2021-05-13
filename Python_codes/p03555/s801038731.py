x = [input() for i in range(2)]
if x[0][0] == x[1][2] and x[0][1] == x[1][1] and x[1][0] == x[0][2]:
  print('YES')
else:
  print('NO')