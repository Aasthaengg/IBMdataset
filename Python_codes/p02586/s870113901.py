R,C,K=map(int,input().split())
G=[[0]*(C+1) for i in range(R+1)]
for i in range(K):
    r,c,v=map(int,input().split())
    G[r][c]=v
dp=[[0]*(C+1) for i in range(R+1)]
for i in range(1,R+1):
    d1,d2,d3=0,0,0
    for j in range(1,C+1):
        v=G[i][j]
        if v!=0:
            if d2!=0:
                d3=max(d3,d2+v)
            if d1!=0:
                d2=max(d2,d1+v)
            d1=max(dp[i-1][j]+v,d1)
        else:
            d1=max(dp[i-1][j],d1)
        dp[i][j]=max(d1,d2,d3)
print(dp[R][C])
