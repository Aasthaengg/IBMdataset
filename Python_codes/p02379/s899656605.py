import math

x1,y1,x2,y2 = map(float,input().split())

x =math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 

print(f'{x:.08f}')



