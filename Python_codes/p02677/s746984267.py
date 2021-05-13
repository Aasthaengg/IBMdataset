import math
from decimal import *
A,B,H,M = map(int,input().split())

h_rad = math.radians((30 * (H + M / 60)))
m_rad = math.radians(6 * M)
diff = abs(h_rad - m_rad)

ans = math.sqrt(pow(A,2) + pow(B,2) - 2 * A * B * math.cos(diff))

print(ans)