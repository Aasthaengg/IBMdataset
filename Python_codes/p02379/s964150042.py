import math

x1,y1,x2,y2=map(float,input().split())

if x1>x2:
    H=x1-x2
else:
    H=x2-x1

if y1>y2:
    W=y1-y2
else:
    W=y2-y1
    
a=math.sqrt(H**2+W**2)

print(a)

