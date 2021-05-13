import math
A,B,H,M=map(int,input().split())
T=H*60+M
theta=2*math.pi*11*T/(12*60)
X=A-B*math.cos(theta)
Y=-B*math.sin(theta)
print(math.sqrt(X**2+Y**2))
