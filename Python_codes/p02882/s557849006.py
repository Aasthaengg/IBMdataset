import math

a,b,x= map(int, input().split())

if x<a*a*b/2:
    a2= x/(a*b/2)
    print(math.degrees(math.atan(b/a2)))
else:
    a3=(a*a*b-x)/(a*a/2)
    print(math.degrees(math.atan(a3/a)))
