import math
a,b,x = map(int,input().split())
if x == a*a*b:
    print(0)
    exit()
if a*a*b/2 < x:
    x = a*a*b - x
    b = x*2/(a*a)
p = x*2/(a*b)
print(math.degrees(math.atan(b/p)))