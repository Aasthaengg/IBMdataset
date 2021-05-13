n,m=list(map(int,input().split()))
l=[]
for i in range(n):
    a=input()
    p=[]
    for i in range(m):
        if a[i]=='#':
            p.append(-1)
        else:
            p.append(0)
    l.append(p)
dp=[[0 for j in range(m)]for i in range(n)]
for i in range(m):
    if l[0][i]!=-1:
        dp[0][i]=1
    else:
        break
for i in range(n):
    if l[i][0]!=-1:
        dp[i][0]=1
    else:
        break
mod=10**9+7
for i in range(1,n):
    
    for j in range(1,m):
        if l[i][j]!=-1:
            
            
                
                
                
            
            dp[i][j]+=((dp[i-1][j])%(mod) + (dp[i][j-1])%mod)%mod
        

print(dp[n-1][m-1])
        
