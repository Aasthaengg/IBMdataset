from decimal import *

L = int(input())

if L%3 ==0:
    L1 = L/3
    print(L1**3)
else:
    print(Decimal(L/3)**3)