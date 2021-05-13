import math
from decimal import Decimal
a, b, c, d = list(map(int, input().split()))

cnt = 0
numc = b//c - math.ceil(Decimal(a)/Decimal(c)) + 1
numd = b//d - math.ceil(Decimal(a)/Decimal(d)) + 1

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

cd = (c*d) // gcd(c, d)
numcd = b//cd - math.ceil(Decimal(a)/Decimal(cd)) + 1

cnt = b - a + 1 - numc - numd + numcd

print(cnt)