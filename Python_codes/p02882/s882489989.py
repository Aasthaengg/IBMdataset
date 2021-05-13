import math
a,b,x = map(int,input().split())
x = x/a

if x >a*b/2:
    theta = math.degrees(math.atan2(2*(a*b-x)/a,a))
else:
    theta = math.degrees(math.atan2(b,2*x/b))
print(theta)