import math as m


a, b, x = map(int, input().split())

if x == b * a**2:
    print(0)

elif x >= b * a**2 / 2:
    y = 2 * (b - x / (a**2))
    print(90 - m.atan(a / y) * 180 / m.pi)
else:
    y = 2 * x / (a * b)
    print(90 - m.atan(y / b) * 180 / m.pi)