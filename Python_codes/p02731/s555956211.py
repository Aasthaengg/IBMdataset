from decimal import Decimal

L = input()
L = Decimal(L)

L = Decimal(L/3)
Ans = Decimal(L*L*L)

print(Ans)