
import decimal

a, b = input().split()
a = decimal.Decimal(a)
b = decimal.Decimal(b)
print(a * int(b * 1000) // 1000)
