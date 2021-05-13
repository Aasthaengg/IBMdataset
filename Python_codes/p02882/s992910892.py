import math
a, b, x = map(int, input().split())
if 2 * x > a**2 * b:
    aa = 2 * a**2 * b - 2 * x
    bb = a**3
else:
    aa = a * b**2
    bb = 2 * x
print(math.degrees(math.atan2(aa, bb)))
