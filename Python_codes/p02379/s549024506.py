import math
x1,y1,x2,y2=map(float,input().split())
dx=abs(x1-x2)
dy=abs(y1-y2)
print(math.sqrt(dx*dx+dy*dy))