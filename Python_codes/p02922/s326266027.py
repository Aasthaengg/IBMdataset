import math
a,b = map(int,input().split())
c = (b - 1) / (a - 1)
c = math.ceil(c)
print(c)
