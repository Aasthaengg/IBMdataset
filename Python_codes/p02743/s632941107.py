from math import sqrt
from decimal import *
a, b, c = map(int, input().split())
if Decimal(a).sqrt() + Decimal(b).sqrt() < Decimal(c).sqrt():
    print('Yes')
else:
    print('No')
