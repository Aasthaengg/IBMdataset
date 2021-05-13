import math
A,B,H,M=map(int,input().split())

theta_hour=math.pi/6*H+math.pi/6*M/60
theta_minute=math.pi/30*M
x=A**2+B**2-2*A*B*math.cos(abs(theta_hour-theta_minute))

print(math.sqrt(x))

