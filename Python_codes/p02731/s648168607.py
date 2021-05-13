from decimal import *
getcontext().prec = 28
n = Decimal(input())
print((n/Decimal(3.0))**Decimal(3))