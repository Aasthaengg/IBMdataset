from decimal import Decimal

x = int(input())

t = 100
n = 0
while t < x:
  t = int(Decimal(t) * Decimal(101) / Decimal(100))
  n += 1
print(n)
