import math
from decimal import Decimal

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

s = min(a, b, c, d, e)

print(math.ceil((n)/(s)) + 4)
