from math import atan2, pi
a, b, x = map(int, input().split())
t = b - x / a / a
if 2 * t <= b:
    print(atan2(2 * t, a) * 180 / pi)
else:
    t = x / b / a
    print(atan2(b, 2 * t) * 180 / pi)
