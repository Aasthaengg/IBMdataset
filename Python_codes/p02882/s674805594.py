import math
a, b, x = map(int, input().split())
A, B = a**2, b**2
print(math.degrees(math.asin((B / ((2 * x / (a * b))**2 + B))**0.5) if 2 * x <=
                   a * a * b else math.acos((A / ((2 * (a * a * b - x) / A)**2 + A))**0.5)))
