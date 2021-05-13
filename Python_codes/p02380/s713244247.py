from math import sin,cos,radians
a,b,c=map(int,input().split())
c=radians(c)
s=a*b*sin(c)*0.5
for i in[s,a+b+(a*a+b*b-2*a*b*cos(c))**0.5,s/a*2]:print('%5f'%i)