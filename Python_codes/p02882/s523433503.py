from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import math

ans = 0
a, b, x = map(int, input().split())
S = x / a
if S >= (a * b / 2):
    h = ((a * b - S) * 2) / a
    deg = math.atan2(h, a) / (math.pi * 2) * 360
else:
    w = 2 * S / b
    deg = math.atan2(b, w) / (math.pi * 2) * 360
print(deg)