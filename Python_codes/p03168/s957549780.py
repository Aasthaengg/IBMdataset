#I
N=int(input())
P=[0]+[float(x) for x in input().split()]

dp=[0 for i in range(N+1)]
for i in range(N+1):
    dp[i]=[0 for j in range(i+1)]

dp[1][0]+=1-P[1]
dp[1][1]+=P[1]
for i in range(1,N):
    for j in range(i+1):
        p=P[i+1]
        dp[i+1][j+1]+=dp[i][j]*p
        dp[i+1][j]+=dp[i][j]*(1-p)
ans=0        
for i in range(int((N-1)/2)+1,N+1):
    ans+=dp[N][i]
    
print(ans)