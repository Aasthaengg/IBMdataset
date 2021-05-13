import math
n,d = map(int,input().split())
c = 0
for i in range(n):
    x,y = map(int,input().split())
    q = math.sqrt(x**2 + y**2)
    if q <= d:
        c+=1
print(c)
