import math

x1,y1,x2,y2=map(float,input().split())
dis2=(x1-x2)**2+(y1-y2)**2

dis = math.sqrt(dis2)
print('{:.8f}'.format(dis))
