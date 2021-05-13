from itertools import combinations_with_replacement

N,M,Q=map(int,input().split())

A,B,C,D=[],[],[],[]

for i in range(Q):
    a,b,c,d=list(map(int,input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

Z=combinations_with_replacement(range(1,M+1),N)

M=0
for K in Z:
    X=0
    L=["*"]+list(K)
    for i in range(Q):
        if L[B[i]]-L[A[i]]==C[i]:
            X+=D[i]
    M=max(M,X)
print(M)
