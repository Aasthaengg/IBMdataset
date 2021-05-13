a,b,x=map(int, input().split())
from decimal import Decimal, DecimalException, getcontext
getcontext().prec = 100
from math import floor
tmp1 = floor(Decimal(b)/Decimal(x))
tmp2 = floor(Decimal(a-1)/Decimal(x))
print(tmp1 - tmp2)