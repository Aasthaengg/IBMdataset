import math

a,b,x = [int(i) for i in input().split()]
s = x / a
if s<=a*b/2:
    print(math.atan(b**2/(2*s))/math.pi*180)
else:
    print(math.atan(2*(a*b-s)/(a**2))/math.pi*180)

