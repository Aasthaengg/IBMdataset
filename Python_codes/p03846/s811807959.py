N=int(input())
A=[int(x) for x in input().split()]
mod=10**9+7
A=sorted(A)

if N%2==0:
    if all(A[i]==A[i+1] and A[0]==1 and A[1]==1 and A[i]-2==A[i-2] for i in range(2,N,2)):
        print((2**(N//2))%mod)
    else:
        print(0)
else:
    if all(A[0]==0 and A[i]==A[i-1] and A[i]-2==A[i-2] and A[-1]==N-1 for i in range(2,N,2)):
        print((2**(N//2))%mod)
    else:
        print(0)
