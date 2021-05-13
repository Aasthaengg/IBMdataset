import math
a, b, x = map(int, input().split())
if a ** 2 * b / 2 <= x:
  theta = math.atan(2 * b / a - 2 * x / (a ** 3))
else:
  theta = math.pi / 2 - math.atan(2 * x / (a * b * b))
print(math.degrees(theta))