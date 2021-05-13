import math
A,B,H,M=map(int,input().split())
t=abs(30*H-5.5*M)
cos_t=math.cos(math.radians(t))
print((A**2+B**2-2*A*B*cos_t)**0.5)