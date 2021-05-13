import math
from decimal import Decimal
a,b,c = map(int,input().split())
x,y,z = [Decimal(a).sqrt(),Decimal(b).sqrt(),Decimal(c).sqrt()]
if x + y < z:
    print('Yes')
else:
    print('No')