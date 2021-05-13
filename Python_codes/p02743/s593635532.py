from decimal import *
import math
getcontext().prec=100
a,b,c=map(int,input().split())
if a+b+2*(Decimal(a).sqrt())*(Decimal(b).sqrt())<c:
  print("Yes")
else:
  print("No")
