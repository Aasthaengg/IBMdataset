import math
a,b,x = list(map(int,input().split()))
if x/a > a*b/2:
    y = 2*b-(2*x)/a**2
    print(math.degrees(math.atan(y/a)))
else:
    y = (2*x)/(a*b)
    print(90-math.degrees(math.atan(y/b)))