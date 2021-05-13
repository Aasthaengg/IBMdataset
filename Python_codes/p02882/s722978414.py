from math import atan, degrees
a,b,x=list(map(int, input().split()))
V=a**2*b
if 2*x<=V:
    t=a*b**2/(2*x)
else:
    t=(2*(V-x))/a**3
print(degrees(atan(t)))