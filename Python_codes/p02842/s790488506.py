from decimal import *

N = int(input())

X = (N / Decimal('1.08')).quantize(Decimal('0'), rounding=ROUND_UP)
if int(X * Decimal('1.08')) == N:
    print(int(X))
else:
    print(':(')