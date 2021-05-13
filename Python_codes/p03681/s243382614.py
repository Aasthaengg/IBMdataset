import sys
import math
n, m = map(int, input().split())

if abs(n-m) > 1:
  print(0)
  sys.exit(0)

c = math.factorial(n) * math.factorial(m)
result = 2 * c if n == m else c
print(result % (10 ** 9 + 7))