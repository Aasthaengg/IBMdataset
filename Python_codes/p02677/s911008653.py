import math
a,b,h,m = map(int, input().split())
cos = math.cos((60*h -11*m)*math.pi/360)
print((a**2 + b**2 -2*a*b*cos)**0.5)