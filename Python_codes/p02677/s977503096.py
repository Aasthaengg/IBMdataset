import math
a, b, h, m = map(int, input().split())
theta = math.pi * abs((h+m/60)/6 - m/30);
val = math.sqrt(a*a + b*b - 2*a*b*math.cos(theta))
print(val)
