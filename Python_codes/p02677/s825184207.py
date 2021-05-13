A,B,H,M=map(int,input().split())

def degh(H,M):
    bdeg=30
    return bdeg*(H+M/60)

import math
theta=math.radians(degh(H,M)-M*360/60)

# print(degh(H,M),M*360/60)

print((A**2+B**2-2*A*B*math.cos(theta))**0.5)