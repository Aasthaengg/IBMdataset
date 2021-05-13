import math

x1,y1,x2,y2 = map(float,input().split())

x_dis = abs(x1-x2)
y_dis = abs(y1-y2)

hypo = math.sqrt(x_dis**2 + y_dis**2)
dis = round(hypo,8)

print(dis)
