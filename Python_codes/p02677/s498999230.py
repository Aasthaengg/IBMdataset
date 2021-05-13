import math
A, B, H, M = map(int, input().split())
D = [(30*H) + (0.5*M), 6*M]
N = max(D) - min(D)
C = math.cos(math.radians(N))
sans = (A**2 + B**2) - (2*A*B*C)
ans = math.sqrt(sans)
print(ans)
