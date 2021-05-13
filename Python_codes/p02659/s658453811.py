import decimal
a, b = input().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
ans = a*b
print(int(ans))