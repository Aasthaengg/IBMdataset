from decimal import Decimal
A, B = map(str, input().split())
ans = Decimal(A)*Decimal(B)
res = int(ans)
print(res)