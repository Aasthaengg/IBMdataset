from math import radians, sqrt, sin, cos
a, b, C = map(float, input().split())
print(a * b * sin(radians(C)) / 2)
print(a + b + sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(C))))
print(b * sin(radians(C)))

