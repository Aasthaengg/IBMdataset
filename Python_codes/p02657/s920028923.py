from decimal import Decimal
a, b = input().split()
a = int(a)
b = float(b)

print(int(Decimal(a*b)))
