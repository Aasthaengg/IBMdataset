from math import floor
import decimal
a,b = map(decimal.Decimal,input().split())
r = floor(a * b)
print(r)
