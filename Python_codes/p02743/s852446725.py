from decimal import Decimal
a, b, c = map(Decimal, input().split())

ans = (c - a - b)**2 > 4 * a * b

if c - a - b < 0:
    ans = False

print("Yes" if ans else "No")