import math
a,b,C = map(float,input().split())
c = math.sqrt( (a*a)+(b*b) - 2*a*b*math.cos(C/180 * math.pi))
h = b * math.sin(C/180 * math.pi)
print(h * a /2)
print(a+b+c)
print(h)