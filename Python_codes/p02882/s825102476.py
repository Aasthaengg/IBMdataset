a, b, x = map(int, input().split())
y = x / (a ** 2)
import math
ans = math.atan((2 * b - 2 * y) / a) * 360 / 2 / math.pi
if 2 * b - 2 * y > b:
  ans = math.atan((b ** 2) / (2 * a * y)) * 360 / 2 / math.pi
print(ans)