from decimal import *

a,b,c = map(int, open(0).read().split())
getcontext().prec = 25
A = Decimal(a).sqrt()
B = Decimal(b).sqrt()
C = Decimal(c).sqrt()
if A + B < C:
    print('Yes')
else:
    print('No')