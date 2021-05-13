n,p,q=map(int,input().split())
M2=-10*(-n//2)
M1=10*(n//2)
dp1=[[float("INF")]*(M1+1)for i in range(M1+1)]
dp1[0][0]=0
for _ in range(n//2):
    a,b,c=map(int,input().split())
    for i in range(M1,a-1,-1):
        for j in range(M1,b-1,-1):
            dp1[i][j]=min(dp1[i][j],dp1[i-a][j-b]+c)
dp2=[[float("INF")]*(M2+1)for i in range(M2+1)]
dp2[0][0]=0
for _ in range(-(-n//2)):
    a,b,c=map(int,input().split())
    for i in range(M2,a-1,-1):
        for j in range(M2,b-1,-1):
            dp2[i][j]=min(dp2[i][j],dp2[i-a][j-b]+c)
ans=float("INf")
for i in range(M1+1):
    for j in range(M1+1):
        for c in range(max(1,-min(-i//p,-j//q)),M2//max(p,q)+1):
            ans=min(ans,dp1[i][j]+dp2[c*p-i][c*q-j])
print(ans if ans!= float("INF") else -1)