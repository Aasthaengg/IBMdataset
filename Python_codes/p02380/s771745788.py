import math

a,b,c = map(int,raw_input().split())
c = math.radians(c)
s = (a*b*math.sin(c))/2
h = b*math.sin(c)
L = a+b+math.sqrt(math.pow(a,2)+math.pow(b,2)-2*a*b*math.cos(c))
print(s)
print(L)
print(h)