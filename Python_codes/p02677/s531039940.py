import math
A,B,H,M = map(int,input().split())

rad = abs((30*H+30*M/60)-6*M)
if rad >= 180:
    rad = 360-rad

c = A**2+B**2-2*A*B*(math.cos(math.radians(rad)))

print(math.sqrt(c))