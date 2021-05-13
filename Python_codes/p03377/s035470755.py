y = input().split()
a = int(y[0])
b = int(y[1])
x = int(y[2])
if a > x or (a+b) < x:
  print('NO')
else:
  print('YES')