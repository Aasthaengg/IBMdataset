import math

a, b, h, m = list(map(int, input().split()))
deg_a = (60 * h + m) * (360 / (60 * 12))
deg_b = m * (360 / 60)
deg = abs(deg_a - deg_b)
rad = math.radians(deg)

c2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)
print(c2 ** 0.5)