import math
n = int(input())
x = n / 2
y = n % 2
if y == 0:
  print(math.floor(x))
else:
  print(math.ceil(x))