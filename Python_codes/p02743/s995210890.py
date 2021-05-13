from decimal import *
a,b,c = map(int,input().split())
getcontext().prec = 50
lhs = Decimal(a).sqrt()+Decimal(b).sqrt()
rhs = Decimal(c).sqrt()
if lhs < rhs:
  print("Yes")
else:
  print("No")