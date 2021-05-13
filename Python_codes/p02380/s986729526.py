import math
a,b,c=map(float,input().split())

S=a*b*math.sin(math.radians(c))/2
h=b*math.sin(math.radians(c))

L= a+b+math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(math.radians(c))))

print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(h))

