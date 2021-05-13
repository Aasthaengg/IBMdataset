import math
a,b,c,d = map(float,input().split())
x = abs(c-a)
y = abs(d-b)
S = (x**2+y**2)**0.5
print(S)
