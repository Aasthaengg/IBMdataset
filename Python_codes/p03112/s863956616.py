import sys
import math
def input():
    return sys.stdin.readline()[:-1]
a,b,q=map(int,input().split())
s=[int(input()) for i in range(a)]
t=[int(input()) for i in range(b)]
x=[int(input()) for i in range(q)]
import bisect

inf=10**11

def tansak(lis,lis2,dis):
    ind=bisect.bisect_left(lis,dis)
    ind2=bisect.bisect_left(lis2,dis)
    return ind,ind2

for i in range(q):
    now = x[i]
    ind,ind2 = tansak(s,t,now)
    if  ind==0:
        one=-inf
    else:
        one=s[ind-1]
    if ind==a:
        two=inf
    else:
        two=s[ind]
    if ind2==0:
        thr=-inf
    else:
        thr=t[ind2-1]
    if ind2==b:
        fo=inf
    else:
        fo=t[ind2]
    tmp1=max(two,fo)-now
    tmp2=2*two-thr-now
    tmp3=2*fo-one-now
    tmp4=now-min(one,thr)
    tmp5=now-thr+two-thr
    tmp6=now-one+fo-one
    print(min(tmp1,tmp2,tmp3,tmp4,tmp5,tmp6))
