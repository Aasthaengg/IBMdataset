from collections import Counter
N=int(input())
A=list(map(int,input().split()))
cnt=[0]*(10**5+10)
for a in A:
    cnt[a]+=1
s=sum(A)
Q=int(input())
for _ in [0]*Q:
    b,c=map(int,input().split())
    s+=cnt[b]*(c-b)
    cnt[c]+=cnt[b]
    cnt[b]=0
    print(s)