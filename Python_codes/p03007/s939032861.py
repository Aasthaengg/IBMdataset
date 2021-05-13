import sys
sys.setrecursionlimit(10**7)
#n,m=map(int,input().split())
n=int(input())
a=[int(i) for i in input().split()]
a.sort()
if a[-1]<=0:
    x=a.pop()
    print(x-sum(a))
    for y in a:
        print(x,y)
        x=x-y
elif a[0]>=0:
    a=a[::-1]
    x=a.pop()
    print(-x+sum(a))
    while a:
        y=a.pop()
        if len(a)>0:
            print(x,y)
            x=x-y
        else:
            print(y,x)
            
else:
    for i in range(n):
        if a[i]>0:
            ap=a[i:]
            an=a[:i]
            break
    print(sum(ap)-sum(an))
    z=ap.pop()
    x=an.pop()
    for y in ap:
        print(x,y)
        x=x-y
    for y in an:
        print(z,y)
        z=z-y
    print(z,x)
