import math
x1, y1, x2, y2 = map(float,input().split())

n = (x2-x1)**2+(y2-y1)**2
N = math.sqrt(n)
print('{:.8f}'.format(N))
