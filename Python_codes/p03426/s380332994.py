H,W,D=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
Q=int(input())
X=[[[0,0] for _ in range((H*W)//D+1)] for _ in range(D)]
for i in range(H):
    for j in range(W):
        X[A[i][j]%D][A[i][j]//D][0]=i
        X[A[i][j]%D][A[i][j]//D][1]=j
M=[[0]*((H*W)//D+1) for _ in range(D)]
for d in range(D):
    for k in range((H*W)//D):
        M[d][k+1]=abs(X[d][k+1][0]-X[d][k][0])+abs(X[d][k+1][1]-X[d][k][1])+M[d][k]

for i in range(Q):
    L,R=map(int,input().split())
    print(M[L%D][R//D]-M[L%D][L//D])