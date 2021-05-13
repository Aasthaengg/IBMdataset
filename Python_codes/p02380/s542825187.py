import math
a,b,c = ((float(x) for x in input().split()))

S = a*b*math.sin(math.radians(c))/2
x = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(c)))
L = a + b + x
h = b*math.sin(math.radians(c))
print(S)
print(L)
print(h)

