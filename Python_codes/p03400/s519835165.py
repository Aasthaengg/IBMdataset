import math
n=int(input())
d,x=map(int,input().split())
a=[0]*n
for i in range(n):
    a[i]=int(input())
    x+=math.ceil(d/a[i])
print(x)