a,b,c,d = map(float,input().split())
x = a-c
y = b-d
from math import sqrt
res = sqrt(x**2+y**2)
print('{0:.6f}'.format(res))
