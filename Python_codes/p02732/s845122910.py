from collections import Counter

N=int(input())
a=list(map(int,input().split()))

A=Counter(a)
B=list(A.keys())
C=list(A.values())

ans=sum(c*(c-1)//2 for c in C)

for k in range(1,N+1):
    print(ans-A[a[k-1]]+1)