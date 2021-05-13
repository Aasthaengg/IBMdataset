from math import sin, cos, pi

a, b, h, m = map(int, input().split())

time = h * 60 + m
half = 12 * 60
x_a = a * cos(2 * pi * time / half)
y_a = a * sin(2 * pi * time / half)
x_b = b * cos(2 * pi * m / 60)
y_b = b * sin(2 * pi * m / 60)
l = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5
print(l)