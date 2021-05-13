import math
a, b = map(int, input().split())
x0 = math.ceil(a * 100 / 8)
x1 = math.ceil((a + 1) * 100 / 8)
y0 = b * 10
y1 = (b + 1) * 10
if y1 <= x0 or x1 <= y0:
    print(-1)
else:
    print(max(x0, y0))