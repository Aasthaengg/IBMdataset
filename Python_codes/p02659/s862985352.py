import decimal
a,b = map(str, input().split())
a = int(a)
b = decimal.Decimal(b)
c = decimal.Decimal(a*b)
d = decimal.Decimal(c//1)
print(d)