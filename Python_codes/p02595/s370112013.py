import math
n,d=map(int,input().split())
c=0
for _ in range(n):
    x,y=map(int,input().split())
    k=math.sqrt(x**2+y**2)
    if k<=d:
        c+=1
print(c)