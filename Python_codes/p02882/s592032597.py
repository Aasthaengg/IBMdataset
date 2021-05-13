import math
from decimal import Decimal
A,B,X = map(Decimal, input().split())
s = X / A

if s == A*B:
    print(0)
    exit()
if s > A * B / 2:
    Bu = 2 * s / A - B
    s -= A*Bu
    B -= Bu

A2 = 2 * s / B
print(math.degrees(math.atan(B/(A2))))
