H,W=map(int,input().split())
A=[input() for i in range(H)]
d=[[0]*(W+1) for i in range(H+1)]
d[0][1]=1
m=10**9+7
for i in range(H):
    for j in range(W):
        if A[i][j]=='.':
            d[i+1][j+1]=(d[i][j+1]+d[i+1][j])%m
print(d[-1][-1])