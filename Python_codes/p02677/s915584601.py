import math
A, B, H, M = map(int,input().split())
t = 60*H + M
tb = (6*t)%360
ta = (360*t/(12*60))%360
c = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(ta-tb)))
print(c)