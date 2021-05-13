import math

a,b,x = map(int,input().split())

h1 = b - x/a/a
h2 = 2*x/(a*b)


if x == a*a*b:
    print(0)
elif b*a*a/2 <= x:
    radians = math.atan(a/2/h1)
    print(90 - math.degrees(radians))
else:
    radians = math.atan(h2/b)
    print(90 - math.degrees(radians))
