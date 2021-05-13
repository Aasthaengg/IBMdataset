import math
x1,y1,x2,y2=map(float,input().split())
xx = (x2-x1)**2
yy = (y2-y1)**2
print(math.sqrt(xx + yy))