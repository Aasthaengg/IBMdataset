import math
xa,ya,xb,yb=map(float, input().split())
print("{0:.8f}".format(math.sqrt( (xa-xb)**2 + (ya-yb)**2 )))