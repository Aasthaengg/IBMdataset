A, B, H, M = map(int, input().split())

import math

C = 360
degS = H*360/12 + M*30/60
degL = M*360/60
rad = (degS-degL)*math.pi / 180
ans = math.sqrt(A*A+B*B-2*A*B*math.cos(rad))
print(ans)