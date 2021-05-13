import math
a,b,C=map(int,input().split())
C=C*math.pi/180
S=a*b*math.sin(C)/2
print(S,a+b+(a*a+b*b-2*a*b*math.cos(C))**.5,2*S/a,sep='\n')
