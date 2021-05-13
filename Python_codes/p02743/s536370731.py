from decimal import *
a,b,c = map(str,input().split())
a,b,c = Decimal.sqrt(Decimal(a)),Decimal.sqrt(Decimal(b)),Decimal.sqrt(Decimal(c))
if a+b < c:
  print("Yes")
else:
  print("No")