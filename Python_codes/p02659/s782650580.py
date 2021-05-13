from decimal import *
A, B = map(str, input().split())
ans = Decimal(A) * Decimal(B)
print(int(ans))