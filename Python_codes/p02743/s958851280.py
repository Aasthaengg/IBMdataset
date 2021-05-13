from decimal import Decimal

a,b,c = (x for x in input().split())

roota = Decimal(a)**Decimal("0.5")
rootb = Decimal(b)**Decimal("0.5")
rootc = Decimal(c)**Decimal("0.5")

if roota + rootb < rootc:
    print("Yes")
else:
    print("No")