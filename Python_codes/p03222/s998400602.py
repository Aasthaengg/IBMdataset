mod=1000000007
H,W,K=map(int,input().split())
dp=[[0]*W for i in range(1+H)]
dp[0][0]=1
C=[0]*(W+1)
C[0]=1
c=[[0,0] for i in range(1+W)]
c[0][0]=1
for i in range(1,1+W):
    c[i][0]=c[i-1][0]+c[i-1][1]
    c[i][1]=c[i-1][0]
for w in range(1,1+W):
    C[w]=c[w][0]
for i in range(H):
    for k in range(W):
        for l in range(k-1,k+2):
            if l<0 or l>=W:
                continue
            x=dp[i][k]*C[min(k,l)]*C[W-1-max(k,l)]%mod
            dp[i+1][l]=(dp[i+1][l]+x)%mod
print(dp[H][K-1])