import math
a,b,x = map(int,input().split())

y = math.atan((a*(b**2))/(2*x))

if b/math.tan(y) <= a:
    print(math.degrees(y))
    
else:
     print(math.degrees(math.atan(2*(a**2*b-x)/(a**3))))