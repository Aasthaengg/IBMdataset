N=int(input())
A=list(map(int,input().split()))

L=sum(A)
X=0
M=float("inf")
for i in range(N-1):
    X+=A[i]
    M=min(M,abs(2*X-L))
print(M)
