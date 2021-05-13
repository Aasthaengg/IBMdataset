from math import pi,cos,sqrt

a,b,h,m = map(int,input().split())

l = sqrt(a**2 + b**2 - 2*a*b*cos(abs(pi*h/6 + pi*m/360 - pi*m/30)))

print(l)