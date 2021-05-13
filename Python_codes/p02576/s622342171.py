import math
n,x,t = map(int,input().split())
a = int(math.ceil(float(n)/x))
print(a*t)
