from decimal import *
from math import sqrt
a, b, c = map(Decimal, input().split())
print('Yes' if a+b+2*(a*b).sqrt() < c else 'No')