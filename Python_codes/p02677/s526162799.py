import math
a, b, h, m = map(int, input().split())
x = (11 * m - 60 * h) * math.pi / 360
y = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(x))
print(y)