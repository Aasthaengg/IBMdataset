from decimal import Decimal
a,b,c = map(Decimal, input().split())
d = Decimal(0.5)
print("Yes" if a**d+b**d < c**d else "No")