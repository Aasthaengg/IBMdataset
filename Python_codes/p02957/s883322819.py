import math
x = input().split()
a = int(x[0]) + int(x[1])
b = math.floor(a / 2)
if (a % 2) == 0:
  print(b)
else:
  print('IMPOSSIBLE')