from math import sin,cos,sqrt,pi
a,b,C=map(float,raw_input().split(" "))
C*=pi/180

c=sqrt(a**2+b**2-2*a*b*cos(C))

L=a+b+c

S=0.5*a*b*sin(C)

h=2*S/a

print S
print L
print h