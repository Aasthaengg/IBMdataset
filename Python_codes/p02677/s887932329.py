import math

a, b, h, m = list(map(int, input().split()))
angle_h = 2 * math.pi * ((60 * h + m) / 720)
angle_m = 2 * math.pi * (m / 60)

diff = angle_m - angle_h
d = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(diff))
print(d)