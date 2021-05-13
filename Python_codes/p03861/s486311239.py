from decimal import *
a, b, x = map(int, input().split())
ax = int(Decimal(a) / Decimal(x))
bx = int(Decimal(b) / Decimal(x))
am = a % x
bm = b % x
if ax == bx and am != 0 and bm != 0:
  print(0)
elif am == 0:
  print(bx - ax + 1)
else:
  print(bx - ax)