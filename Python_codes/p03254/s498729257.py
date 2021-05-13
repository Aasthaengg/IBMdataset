n,x=map(int,input().split())
a=list(map(int,input().split()))

res=0
i=0
a.sort()

while 0<x and i < n:
    if a[i] <= x:
        res+=1
    x-=a[i]
    i+=1
if 0 < x:
    print(res-1)
else:
    print(res)