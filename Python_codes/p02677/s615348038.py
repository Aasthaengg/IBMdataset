import math

a, b, h, m = map(int, input().split())

rad_h = (h + m / 60) / 12
rad_m = m / 60
# print(rad_h, rad_m)

if rad_h >= rad_m:
	rad = rad_h - rad_m
else:
	rad = rad_m - rad_h
if rad >= 0.5:
	rad = 1 - rad
rad *= math.pi * 2

# print(rad)
print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)))