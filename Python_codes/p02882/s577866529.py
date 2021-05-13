import math
a,b,x = map(int,input().split())
if x >= (a**2*b)/2:
    print(math.degrees(math.atan((2*b-2*x/a**2)/a)))
else:
    print(90-math.degrees(math.atan(2*x/(a*b**2))))