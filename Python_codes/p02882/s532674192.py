import math
a,b,x=map(int,input().split())

bottle=(a**2)*b
#空間が三角柱か四角柱の境目の時の角度r
r=b/a

theta=2*(bottle-x)/(a**3)
theta=math.degrees(math.atan(theta))

if 2*x>(a**2)*b:
    print(theta)
else:
    theta=(a*(b**2))/(2*x)
    print(math.degrees(math.atan(theta)))