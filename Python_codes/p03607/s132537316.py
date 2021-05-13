from itertools import groupby

N=int(input())
A=[int(input()) for i in range(N)]

A=sorted(A)

ans=0
for i,k in groupby(A):
    if (len(list(k)))%2==1:
        ans+=1

print(ans)