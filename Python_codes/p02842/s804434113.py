import math

n = int(input())

without_tax = float(n/1.08)
without_tax_floor = math.floor(without_tax)
without_tax_ceil = math.ceil(without_tax)

if math.floor(without_tax_floor * 1.08) == n:
    print(without_tax_floor)
elif math.floor(without_tax_ceil * 1.08) == n:
    print(without_tax_ceil)
else:
    print(':(')