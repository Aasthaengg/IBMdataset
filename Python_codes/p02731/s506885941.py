from decimal import Decimal

l = input()

t = Decimal(l) / Decimal("3")
v = t ** 3

print(v)