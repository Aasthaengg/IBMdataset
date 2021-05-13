import itertools
from bisect import bisect_left
A,B,Q=map(int,input().split())
s=[int(input()) for i in range(A)]
t=[int(input()) for i in range(B)]
x=[int(input()) for i in range(Q)]

for i in range(Q):
    bs=bisect_left(s,x[i])
    bt=bisect_left(t,x[i])
    sli=[];bli=[]
    if(bs!=A):
        sli.append(s[bs])
    if(bs!=0):
        sli.append(s[bs-1])
    if(bt!=B):
        bli.append(t[bt])
    if(bt!=0):
        bli.append(t[bt-1])

    res=10**30
    for p in itertools.product(sli,bli):
        if(p[0]<=x[i] and p[1]<=x[i]):
            res=min(res,x[i]-min(p))
        elif(p[0]>=x[i] and p[1]>=x[i]):
            res=min(res,max(p)-x[i])
        else:
            res=min([res,abs(p[1]-x[i])*2+abs(p[0]-x[i]),abs(p[1]-x[i])+abs(p[0]-x[i])*2])
    print(res)