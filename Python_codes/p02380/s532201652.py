import math
a,b,c = map(int,input().split())
c = math.radians(c)
s = a*b*math.sin(c)/2
cr = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c))
l = a + b + cr
h = b*math.sin(c)
print(s,l,h)
