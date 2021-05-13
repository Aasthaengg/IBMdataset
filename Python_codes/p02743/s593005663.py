a, b, c = map(int,input().split())

from decimal import *

getcontext().prec = 100



if (a + b + 2*(Decimal(a).sqrt())*(Decimal(b).sqrt()) < c):
    print('Yes')
else:
    print('No')
