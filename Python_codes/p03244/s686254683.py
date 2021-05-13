N=int(input())
V=list(map(int,input().split()))

A={0:0}
B={0:0}
for i in range(N):
    v=V[i]
    if i%2==0:
        if v in A:
            A[v]+=1
        else:
            A[v]=1
    else:
        if v in B:
            B[v]+=1
        else:
            B[v]=1

P=max(A,key=lambda x:A[x])
Q=max(B,key=lambda x:B[x])

if P!=Q:
    print(N-(A[P]+B[Q]))
else:
    X=A[P]
    del A[P]
    R=max(A,key=lambda x:A[x])

    Y=B[Q]
    del B[Q]
    S=max(B,key=lambda x:B[x])

    print(N-max(X+A[R],Y+B[S]))
