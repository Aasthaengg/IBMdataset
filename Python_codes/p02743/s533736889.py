from decimal import *
a, b, c = map(int, input().split())
a = Decimal(str(a))
b = Decimal(str(b))
c = Decimal(str(c))
if a.sqrt() + b.sqrt() < c.sqrt():
  print("Yes")
else:
  print("No")
