import decimal

a, b, c = map(int, input().split())
a, b, c = decimal.Decimal(a), decimal.Decimal(b), decimal.Decimal(c)

if a.sqrt() + b.sqrt() < c.sqrt():
    print("Yes")
else:
    print("No")
