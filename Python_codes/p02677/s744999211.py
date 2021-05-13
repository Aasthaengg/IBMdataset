import math
A, B, H, M = map(int, input().split())

t1 = math.radians(M * 360 / 60)
x1 = B * math.sin(t1)
y1 = B * math.cos(t1)

t2 = math.radians((H * 60 + M) * 360 / (12 * 60))
x2 = A * math.sin(t2)
y2 = A * math.cos(t2)

ans = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(ans)