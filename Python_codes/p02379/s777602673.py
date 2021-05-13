import math
x1,y1,x2,y2=map(float,input().split())
dx,dy=x2-x1,y2-y1
d=math.sqrt(dx*dx+dy*dy)
print("{:.8f}".format(d))
