import math

x1,y1,x2,y2=map(float,input().split())
answer=(math.sqrt((x2-x1)**2+(y2-y1)**2))
print("{0:.8f}".format(answer))