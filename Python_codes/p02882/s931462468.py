import math

a,b,x=map(int,input().split())

if x==a**2*b:
    print(0.0)
elif x>a**2*b/2:
    print(90.0-math.degrees(math.atan(a**3/(2*a**2*b-2*x))))
else:
    print(90.0-math.degrees(math.atan(2*x/(a*b**2))))
