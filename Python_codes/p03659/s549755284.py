N=int(input())
A=list(map(int,input().split()))

S=sum(A)

X=0
D=float("inf")
for i in range(N):
    X+=A[i]

    if i!=N-1:
        Y=S-X
        D=min(D,abs(X-Y))
print(D)