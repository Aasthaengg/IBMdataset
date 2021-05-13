from decimal import Decimal

n = input().split()
print(int(Decimal(n[0]) * Decimal(n[1])))