import math
a, b, h, m = map(int, input().split())
deg_time = 30 * h + m / 2
deg_minute = 6 * m
ans = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(deg_minute - deg_time)))
print(ans)