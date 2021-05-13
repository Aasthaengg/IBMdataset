a, b, h, m = map(int, input().split())

t = h + (m / 60)

# 時針の角度
a_deg = 360 * (t / 12)
# 分針の角度
b_deg = 360 * (m / 60)

# 余弦定理
import math
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(abs(a_deg-b_deg))))

print(c)
