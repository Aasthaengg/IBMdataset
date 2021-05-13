from math import *
s=int(input())
x1=ceil(sqrt(s))
if x1>10**9:
    x1-=1
y2=ceil(s/x1)
if y2>10**9:
    y2-=1
x2=x1*y2-s
print(0,0,x1,1,x2,y2)