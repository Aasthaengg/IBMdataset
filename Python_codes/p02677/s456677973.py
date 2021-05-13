import math
a, b, h, m = map(int, input().split())

angle_a = h*360/12 + m*360/60/12
angle_b = m*360/60
ax = a * math.sin(math.radians(angle_a))
ay = a * math.cos(math.radians(angle_a))
bx = b * math.sin(math.radians(angle_b))
by = b * math.cos(math.radians(angle_b))
print(math.sqrt(abs(ax-bx)**2 + abs(ay-by)**2))