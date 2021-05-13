from decimal import Decimal
A, B, C = map(int, input().split())

if A*B*C%2==0:
    print(0)
else:
    big = max([A, B, C])
    print((A*B*C/Decimal(big)))