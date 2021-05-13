# coding: utf-8
# Your code here!

N=int(input())
A=list(map(int,input().split()))

log=[0]*10**5

for a in A:
    log[a-1]+=1


wa=sum([(i+1)*log[i] for i in range(len(log))])

for _ in range(int(input())):
    B,C=map(int,input().split())
    wa+=(C-B)*log[B-1]
    log[B-1],log[C-1]=0,log[B-1]+log[C-1]
    print(wa)

