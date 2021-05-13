# -*- coding: utf-8 -*-
n=int(input())
a=list(map(int,input().split()))
count1=0
sum1=a[0]
if a[0]==0:
    count1=1
    sum1=1
for ii in range(1,n):
    S=sum1
    sum1+=a[ii]
    if sum1*S>=0:
        if S>0:
            count1+=sum1+1
            sum1=-1
        elif S<0:
            count1+=1-sum1
            sum1=1

if a[0]>=0:
    count2=a[0]+1
    sum2=-1
else:
    count2=1-a[0]
    sum2=1
for ii in range(1,n):
    S=sum2
    sum2+=a[ii]
    if sum2*S>=0:
        if S>0:
            count2+=sum2+1
            sum2=-1
        elif S<0:
            count2+=1-sum2
            sum2=1

print(min(count1,count2))
