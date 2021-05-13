import math

a, b, x = map(int,input().split())

if 2 *x <= a ** 2 * b:
    p1 = a * b ** 2
    p2 = 2 * x
else:
    p1 = 2 * (a ** 2 * b - x)
    p2 = a ** 3

sit = math.atan(p1 / p2)
print(math.degrees(sit))
