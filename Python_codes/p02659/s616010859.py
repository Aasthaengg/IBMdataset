from decimal import Decimal

a,b = map(str,input().split())
a = Decimal(a)
b = Decimal(b)
ans = (a*b)
print(int(ans))
