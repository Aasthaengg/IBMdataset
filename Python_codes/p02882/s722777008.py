from math import atan,pi
a,b,x=map(int,input().split())
if a*a*b>2*x:
  h=2*x/(a*b)
  print(90-atan(h/b)*180/pi)
else:
  h=2*(a*a*b-x)/(a*a)
  print(atan(h/a)*180/pi)