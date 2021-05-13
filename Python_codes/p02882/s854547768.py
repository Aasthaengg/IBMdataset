import math

a, b, x = map(int, input().split())

if x >= a ** 2 * b / 2:
    tan_theta = 2 * (a ** 2 * b - x) / (a ** 3)
    theta = math.atan(tan_theta)
    print(math.degrees(theta))
else:
    tan_theta = 2 * x / (a * b ** 2)
    theta = math.atan(tan_theta)
    print(90 - math.degrees(theta))
