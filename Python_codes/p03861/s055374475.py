from decimal import * 
a, b, x = map(str, input().split())
a = Decimal(a)
b = Decimal(b)
x = Decimal(x)

ans = int(b / x) - int(a / x)

if a % x == 0:
  ans += 1

print(int(ans))




