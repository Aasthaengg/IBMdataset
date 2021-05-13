a,b,x=map(int,input().split())
import math
if x>=a**2*b//2:
    rad=math.atan2(2*(a**2*b-x)/a**2,a)
else:
    rad=math.atan2(b,2*x/a/b)

print(math.degrees(rad))