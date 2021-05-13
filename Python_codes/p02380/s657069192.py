#64 三角形

a, b, c= map(int, input().split())

import math
h = b*math.sin(math.radians(c))
cosc = math.cos(math.radians(c))

S = a*h*(1/2) 

d = math.sqrt((a-(b*cosc))**2 + h**2)

L = a + b + d

print(S)
print(L)
print(h)
