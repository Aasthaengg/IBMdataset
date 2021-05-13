import math
a, b, n = map(int, input().split())
if b > n:
  print(math.floor(a * n / b))
  quit()
else:
  print(math.floor(a - a / b))
