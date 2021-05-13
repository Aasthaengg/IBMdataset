import math
x1,y1,x2,y2 = map(float,input().split())

x_d = x2 - x1
y_d = y2 - y1
print("%0.5f" % math.sqrt(x_d**2 + y_d**2))