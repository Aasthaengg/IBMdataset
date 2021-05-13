# 20-08-12 再トライ
from math import degrees, atan2

a, b, x = [int(x) for x in input().split()]
if x <= a ** 2 * b / 2:
    ans = degrees(atan2(a * b ** 2, 2 * x))
else:
    ans = degrees(atan2(2 * a ** 2 * b - 2 * x, a ** 3))

print(ans)