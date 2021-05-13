from decimal import Decimal

lst = [i for i in input().split()]
z = Decimal(lst[0]) * Decimal(lst[1])
print(int(z))