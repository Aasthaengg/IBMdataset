from math import ceil
from decimal import Decimal, getcontext
getcontext().prec = 100
N = int(input())
TA = [tuple(map(int, input().split())) for _ in range(N)]

T = 1
A = 1
for i in range(N):
    x, y = TA[i]
    n = max(ceil(Decimal(T)/Decimal(x)), ceil(Decimal(A)/Decimal(y)))
    T = n*x
    A = n*y
print(T+A)