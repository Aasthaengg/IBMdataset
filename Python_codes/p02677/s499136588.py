import math
A, B, H, M = map(int, input().split())
m = H*60 + M
a_rad = m / (60 * 12) * math.pi * 2
b_rad = M / 60 * math.pi * 2
ans = (A*A + B*B - 2*A*B*math.cos(a_rad-b_rad))**0.5
print(ans)
