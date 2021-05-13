from decimal import Decimal
a,b,c = map(Decimal,input().split())
x = Decimal(0.5)
if a**x+b**x < c**x:
    print("Yes")
else:
    print("No")