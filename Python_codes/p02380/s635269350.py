# Starting here
#define Pi 3.14159265
import math

def Sin(n):
    return math.sin(n*math.pi/180)

def Cos(n):
    return math.cos(n*math.pi/180)

a,b,ang=map(float,raw_input().split())
A=a*a
B=b*b
area=(0.5*a*b*Sin(ang))
C=A+B-(2*a*b*(Cos(ang)))
c=float(math.sqrt(C))
s=a+b+c
print round(area,5)
print round(s,5)
print round((area*2)/a,5)


