import math
a,b,x = list(map(int, input().split()))
volume = a*a*b
if 2 * x <= volume:
    print(90 - math.degrees(math.atan(2*(x/b/a)/b)))
else:
    print(math.degrees(math.atan(2*(volume-x)/a/a/a)))
