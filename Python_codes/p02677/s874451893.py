import math
A, B, H, M = map(int, input().split())
k = (60 * H - 11 * M)/2
if abs(k) > 180:
    cos = math.cos(math.radians(360-k))
else:
    cos = math.cos(math.radians(k))

a2 = A**2 + B**2 - 2* A* B* cos

print(a2**0.5)
