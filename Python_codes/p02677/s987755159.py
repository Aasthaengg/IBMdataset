A,B,H,M = map(int,input().split())
from math import pi,cos
m = 2*pi * M / 60
h = 2*pi * (H*60 + M) / 720

ans = (A*A + B*B - 2*A*B*cos(abs(m-h))) ** 0.5
print(ans)