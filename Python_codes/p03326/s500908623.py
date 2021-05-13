n,m = map(int, input().split())
l = []
for i in range(n):
    tmp = list(map(int,input().split()))
    l.append(tmp)

if m==0:
    print(0)
    exit()

ans=-10**9
from itertools import *
for tmp in list(product([True,False], repeat=3)):
    lis=[]
    for x in l:
        sm=0
        if tmp[0]:
            sm+=x[0]
        else:
            sm-=x[0]
        if tmp[1]:
            sm+=x[1]
        else:
            sm-=x[1]
        if tmp[2]:
            sm+=x[2]
        else:
            sm-=x[2]

        lis.append(sm)

    lis.sort()

    sm=sum(lis[-m:])
    if ans < sm:
        ans=sm
print(ans)