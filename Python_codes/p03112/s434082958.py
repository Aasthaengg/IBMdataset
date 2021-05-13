from bisect import *
a,b,q=map(int,input().split())
s,t=[],[]
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x=int(input())
    bs=bisect_left(s,x)
    if bs!=0:
        sl=x-s[bs-1]
    else:
        sl=float("inf")
    if bs!=a:
        sr=s[bs]-x
    else:
        sr=float("inf")
    bt=bisect_left(t,x)
    if bt!=0:
        tl=x-t[bt-1]
    else:
        tl=float("inf")
    if bt!=b:
        tr=t[bt]-x
    else:
        tr=float("inf")
    print(min(max(sl,tl),max(sr,tr),2*sl+tr,2*tl+sr,sl+tr*2,tl+sr*2))
