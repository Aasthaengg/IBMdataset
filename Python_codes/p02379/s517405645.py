import math
x1, y1, x2, y2 = map(float, input().split())
x3 = x2 - x1
y3 = y2 - y1
ans = math.hypot(x3, y3)
print(ans)
