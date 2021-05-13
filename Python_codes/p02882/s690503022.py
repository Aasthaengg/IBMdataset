a,b,x = map(int,input().split())
x /= a
import math
PI = math.pi
if x > a*b//2:
    print("{:.10}".format(math.atan2((a*b-x)*2, a*a)*180/PI))
else:
    print("{:.10}".format(math.atan2(b*b,x*2)*180/PI))
