import math
a,b,x = map(int,input().split())
if a**2*b < 2*x:
    print(math.degrees(math.atan(2*b/a - 2*x/a**3 )))
else:
    print(math.degrees(math.atan(a*b*b/(2*x))))