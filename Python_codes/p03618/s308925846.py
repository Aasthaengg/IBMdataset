from itertools import groupby

A=input()
N=len(A)
A=[A[i] for i in range(0,N)]
A.sort()
data=groupby(A)
ans=N*(N-1)//2+1
for key, group in data:
    g=len(list(group))
    ans-=g*(g-1)//2

print(ans)