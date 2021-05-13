import math as m
from decimal import *
a,b,x = map(int,input().split())
tot = b-a+1
rem = a%x
getcontext().prec = 100
if rem > 0:
  tot-=x-rem
print(m.ceil(Decimal(tot)/Decimal(x)))