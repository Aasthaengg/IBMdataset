import decimal
import math

A, B = input().split()
N = decimal.Decimal(A) * decimal.Decimal(B)

print(math.floor(N))