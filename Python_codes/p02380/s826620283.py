from math import sin,cos,radians, sqrt
a,b,C = map(float, input().split())
#面積
C = radians(C)
print('{:.08f}'.format(0.5*a*b*sin(C)))
#辺の長さ
L = a + b + sqrt(a**2 + b**2 -2*a*b*cos(C))
print('{:.08f}'.format(L))
#高さ
print('{:.08f}'.format(b*sin(C)))
