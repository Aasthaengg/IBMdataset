from decimal import Decimal

T, X = [Decimal(i) for i in input().split()]
ans = T / X
print(ans)