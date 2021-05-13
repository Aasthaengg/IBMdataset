import math

a, b, c = map(int, input().split())

print(int((b**2 + c**2 - 2 * b * c * math.cos(math.atan(a / b)))**0.5 * b // 2))