#ITP1_10-B Triangle
import math as m
a,b,C = map(float,input().split(" "))
C = m.pi*C/180
h = b*m.sin(C)
print( a*h*0.5 )
print( (a**2+b**2 - 2*a*b*m.cos(C))**0.5 + a + b )
print( h )   