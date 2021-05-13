import math

A, B, H, M = map(int, input().split())

h = (H/12 + (M/60)/12) * 360
m = (M/60) * 360
r = math.radians(h - m)
ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(r))

print(ans)