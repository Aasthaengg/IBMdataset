import math
a, b, x = map(int, input().split())
if x <= a * a * b / 2:
    t = 2 * x / a / b
    theta = math.atan2(b, t) / math.pi * 180
else:
    y = a * a * b - x
    t = 2 * y / a / a
    theta = math.atan2(t, a) / math.pi * 180
print(theta)