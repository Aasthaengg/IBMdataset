from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

import math

N = int(input())

X = N / 1.08
# X = Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

X = int(math.ceil(X))

if N == int(X * 1.08):
  print(X)
else:
  print(':(')

