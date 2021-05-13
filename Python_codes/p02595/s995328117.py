import math  

n,d=map(int,input().split())
count=0
for i in range(n):
    x,y=list(map(int,input().split()))
    dis = x**2+y**2
    dis = math.sqrt(dis)
    if dis <= d:
        count += 1
print(count)