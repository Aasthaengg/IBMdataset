#C
A, B, H, M= map(int,input().split())
import math
theta_S=-(30*H+(1/2)*M)+90
theta_L=-(6*M)+90
S_x=A*math.cos(math.radians(theta_S))
S_y=A*math.sin(math.radians(theta_S))
L_x=B*math.cos(math.radians(theta_L))
L_y=B*math.sin(math.radians(theta_L))
distance=((S_x-L_x)**2+(S_y-L_y)**2)**0.5
print(distance)