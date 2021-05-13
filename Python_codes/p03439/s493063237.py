from math import *
n=int(input())
mi,mx=0,n-1
print(mi)
t1=input()
if t1=="Vacant":
    exit()
print(mx)
t2=input()
if t2=="Vacant":
    exit()
while True:
    mid=ceil((mi+mx)/2)
    print(mid)
    t2=input()
    if t2=="Vacant":
        exit()
    sa=mid-mi
    if sa%2==0:
        if t1==t2:
            mi=mid
            t1=t2
        else:
            mx=mid
    else:
        if t1==t2:
            mx=mid
        else:
            mi=mid
            t1=t2