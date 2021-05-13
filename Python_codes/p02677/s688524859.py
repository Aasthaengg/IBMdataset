import math
A,B,H,M=list(map(int,input().split()))
r=math.radians(30*H-5.5*M)
print(math.sqrt(A**2+B**2-2*A*B*math.cos(r)))