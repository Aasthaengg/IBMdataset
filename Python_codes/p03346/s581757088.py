import bisect

N=int(input())

A=[int(input())for i in range(N)]
#print(A)

L=[0 for i in range(N+1)]

for i in range(N):
    if L[A[i]-1]>0:
        L[A[i]]=(L[A[i]-1]+1)
    else:
        L[A[i]]=1
print(N-max(L))