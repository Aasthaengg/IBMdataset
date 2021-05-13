from copy import copy

H,W,K=map(int,input().split())
S=[[0]*W for _ in range(H)]

for y in range(H):
    T=input()

    for x in range(W):
        if T[x]=="#":
            S[y][x]=1


C=[[0]*W for _ in range(H)]
T,P=1,-1
for y in range(H):
    F=False
    M=0
    for x in range(W):
        if S[y][x]==1:
            F=True
            for k in range(M,x+1):
                C[y][k]=T
            T+=1
            M=x+1

    if M!=W:
        for k in range(M,W):
            C[y][k]=T-1

    if F:
        for l in range(P+1,y):
            C[l]=copy(C[y])
        P=y

for l in range(P+1,H):
    C[l]=copy(C[P])

G=[" ".join(map(str,x)) for x in C]
print("\n".join(G))