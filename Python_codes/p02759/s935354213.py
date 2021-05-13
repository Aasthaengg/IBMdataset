from decimal import Decimal, ROUND_HALF_UP

n = int(input())
print(Decimal(n/2).quantize(Decimal(0), rounding=ROUND_HALF_UP))