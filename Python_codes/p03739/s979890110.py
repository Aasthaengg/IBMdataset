n=int(input())
a=list(map(int,input().split()))
from itertools import accumulate
from copy import copy
A=list(accumulate(a))
'''
if a[0]<0:
    temp=0
    count=0
    for i in range(1,n):
        if i%2==1:
'''
def seq(xc:list):
    x=copy(xc)
    n=len(x)
    temp1=0
    count1=0
    for i in range(n):
        x[i]+=temp1
        if i%2==1:
            if x[i]<=0:
                count1+=(1-x[i])
                temp1+=(1-x[i])
        else:
            if x[i]>=0:
                count1+=(x[i]+1)
                temp1-=(x[i]+1)
    temp2=0
    count2=0
    for j in range(n):
        xc[j]+=temp2
        if j%2==1:
            if xc[j]>=0:
                count2+=(xc[j]+1)
                temp2-=(xc[j]+1)
        else:
            if xc[j]<=0:
                count2+=(1-xc[j])
                temp2+=(1-xc[j])
    
    return min(count1,count2)
    

print(seq(A))
