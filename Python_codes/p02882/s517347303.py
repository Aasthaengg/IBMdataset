import math

a,b,x = map(int,input().split())

if x == (a**2)*b:
    ans = 90
elif x == (a**2)*b/2:
    ans = 45
elif x < (a**2)*b/2:
    rad = math.atan(2*x/(a*b**2))
    ans = math.degrees(rad)
else:
    rad = math.atan(a**3/(2*a**2*b - 2*x))
    ans = math.degrees(rad)
print(90-ans)