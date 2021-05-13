from math import sqrt
x1,x2,y1,y2=map(float,input().split())
a=abs(x1-y1)**2
b=abs(x2-y2)**2
s=sqrt(a+b)
print(s)
