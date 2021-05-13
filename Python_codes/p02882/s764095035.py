import math
a,b,x = map(int, input().split())

if a*a*b == x:
    print(0)
    exit()

tan = (a*a*a)/(2*(a*a*b-x))
tan_thre = a/b

if tan > tan_thre:
    ans = math.degrees(math.atan(tan))
    print(90-ans)
else:
    tan = 2*x/(a*b*b)
    ans = math.degrees(math.atan(tan))
    print(90-ans)