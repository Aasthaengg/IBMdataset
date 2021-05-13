import math
a, b, h, m = [int(x) for x in input().split(' ')]
print((a**2 + b**2 - 2 * a * b * math.cos(math.radians(h * 330 + m * 5.5)))**0.5)