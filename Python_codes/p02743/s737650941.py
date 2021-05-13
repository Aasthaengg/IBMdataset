from decimal import Decimal
a, b, c = map(str, input().split())
if Decimal(a)**Decimal("0.5") + Decimal(b)**Decimal("0.5") < Decimal(c)**Decimal("0.5"):
    print("Yes")
else:
    print("No")