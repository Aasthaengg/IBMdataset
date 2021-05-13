import math

A,B,H,M = list(map(int, input().split()))
if H == 0:
    H_angle = (360/720)*M
    M_angle = 6*M
else:
    H_M = H*60
    H_angle = (360/720)*(H_M + M)
    M_angle = 6*M

dif = H_angle-M_angle
cos = math.cos(math.radians(H_angle-M_angle))
ans = A**2 + B**2 -2*A*B*cos
print(math.sqrt(ans))
