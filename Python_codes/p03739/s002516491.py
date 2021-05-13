# coding: utf-8
n=int(input())
A=list(map(int,input().split()))

S1=0
cost1=0
for i in range(n):
    if i%2==0:
        if S1+A[i]>0:
            S1+=A[i]
        else:
            cost1+=abs(S1+A[i])+1
            S1=1
    else:
        if S1+A[i]<0:
            S1+=A[i]
        else:
            cost1+=abs(S1+A[i])+1
            S1=-1

S2=0
cost2=0
for i in range(n):
    if i%2==0:
        if S2+A[i]<0:
            S2+=A[i]
        else:
            cost2+=abs(S2+A[i])+1
            S2=-1
    else:
        if S2+A[i]>0:
            S2+=A[i]
        else:
            cost2+=abs(S2+A[i])+1
            S2=1
    
print(min(cost1,cost2))