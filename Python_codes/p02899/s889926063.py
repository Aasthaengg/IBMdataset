N=int(input())
A=list(map(int,input().split()))
L=[0]*N
for i in range(N):
    L[A[i]-1]=i+1
L=[str(a) for a in L]
print(' '.join(L))