def p(x):
  print('{0:.6f}'.format(x))
from math import sqrt,sin,cos,pi

a,b,C = map(float,input().split())
theta = pi*C/180
h,c = 0.0,0.0

if theta<=pi/2:
  h = b*sin(theta)
  x = sqrt(b*b-h*h)
  c = sqrt(h**2+(a-x)**2)

else:
  phi = theta-pi/2
  h = b*cos(phi)
  d = b*sin(phi)
  e = a*h/(a+d)
  f = sqrt(d**2+(h-e)**2)
  g = sqrt(a**2+e**2)
  c = f+g

S = a*h/2
L = a+b+c
p(S)
p(L)
p(h)
