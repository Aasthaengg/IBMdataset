import math

a, b, h, m = map(int, input().split())

ang = h * 30 - m * 11/2

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(ang)))

print(c)
