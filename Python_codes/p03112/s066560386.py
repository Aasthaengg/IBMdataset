from bisect import bisect_left
import sys
def input():
    return sys.stdin.readline()[:-1]
A,B,Q=map(int,input().split())
s=[int(input()) for i in range(A)]
t=[int(input()) for i in range(B)]
for i in range(Q):
    x=int(input())
    si=bisect_left(s,x)
    ti=bisect_left(t,x)
    a=[]
    if si and si!=A:
        sl=s[si-1]
        sr=s[si]
    elif si:
        sl=s[-1]
        sr=0
    else:
        sl=0
        sr=s[0]
    if ti and ti!=B:
        tl=t[ti-1]
        tr=t[ti]
    elif ti:
        tl=t[-1]
        tr=0
    else:
        tl=0
        tr=t[0]
    if sl and tl:
        a.append(x-min(sl,tl))
    if sr and tr:
        a.append(max(tr,sr)-x)
    if sl and tr:
        a.append(tr-x+tr-sl)
        a.append(x-sl+tr-sl)
    if sr and tl:
        a.append(x-tl+sr-tl)
        a.append(sr-x+sr-tl)
    print(min(a))