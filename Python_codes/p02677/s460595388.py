import math
A,B,H,M=map(int,input().split())
b=2*math.pi*(M/60)
a=2*math.pi*((H/12) + (M/(60*12)))
t=abs(a-b)
if t>math.pi:
  t=2*math.pi-t
print(math.sqrt(A**2+B**2-2*A*B*math.cos(t)))