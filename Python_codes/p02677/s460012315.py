import math
A, B, H, M = map(int, input().split())
h = 360 / 12 * H + 0.5 * M
m = 6 * M
hm = abs(h - m)
if hm > 180:
    hm = 360 - hm
rad = math.radians(hm)
ans = A*A + B*B - 2*A*B*math.cos(rad)
print(ans**0.5)