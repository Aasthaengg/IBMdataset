import math
x1,y1,x2,y2=map(float,input().split())
X=x2-x1
Y=y2-y1
L=math.sqrt(X**2+Y**2)
print(f'{L:.8f}')

