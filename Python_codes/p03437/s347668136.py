import math
a, b = map(int, input().split())
if(a % b == 0):
  print(-1)
else:
  i = math.gcd(a, b)
  c = a // i
  d = b // i
  print(c * d * i + a)