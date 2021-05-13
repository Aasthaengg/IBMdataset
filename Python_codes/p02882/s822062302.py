import math

a, b, x = map(int, input().split())

half = a*a*b/2
if half == x:
    print(45)
elif half > x:
    print(math.degrees(math.atan(a*b*b/(x*2))))
else:
    print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))