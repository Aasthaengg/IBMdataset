H,W,D=map(int,input().split())
L=["*"]*(H*W)

for y in range(H):
    B=list(map(int,input().split()))
    for x in range(W):
        L[B[x]-1]=(x,y)

G=[[0]*((H*W+D-1)//D) for _ in range(D)]

for i in range(H*W-D):
    (X1,Y1)=L[i]
    (X2,Y2)=L[i+D]

    p,q=i//D,i%D
    G[q][p+1]=G[q][p]+abs(X1-X2)+abs(Y1-Y2)

Q=int(input())
X=[0]*Q

for k in range(Q):
    L,R=map(int,input().split())
    L,R=L-1,R-1

    p,r=L//D,L%D
    q=R//D
    X[k]=G[r][q]-G[r][p]

print("\n".join(map(str,X)))
