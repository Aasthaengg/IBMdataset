from decimal import Decimal
A, B = input().split()
A = Decimal(A)
B = Decimal(B)
C = A*B
print(int(C))
