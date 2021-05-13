INF=10**18
N,M=map(int,input().split())

a,c=[],[]
for i in range(M):
    A,B=map(int,input().split())  
    C=list(map(int,input().split()))
    tmp=0
    for j in range(B):
      tmp+=1<<(C[j]-1)
    a.append(A)
    c.append(tmp)
    
dp=[[INF]*(1<<N) for i in range(M+1)]
dp[0][0]=0
for i in range(M):
    for j in range(1<<N):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        o=(j | c[i])
        dp[i+1][o]=min(dp[i+1][o],dp[i][j]+a[i])
ans=dp[M][2**N-1]
print(ans if ans!=INF else -1)