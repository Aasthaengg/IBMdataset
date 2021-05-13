import math
x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
if b - (a * c) > 0:
  print(c)
else:
  print(math.floor(b / a))