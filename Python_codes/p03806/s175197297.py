INF=float('inf')
N,Ma,Mb=map(int,input().split())

abc=[]
dp=[[INF]*401 for i in range(401)]
dp[0][0]=0

for i in range(N):
    a,b,c=map(int,input().split())
    for A in reversed(range(401)):
        for B in reversed(range(401)):
            if B-b>=0 and A-a>=0:
                dp[A][B]=min(dp[A][B],dp[A-a][B-b]+c)
ans=INF
for i in range(1,401):
    if i*Ma>400 or i*Mb>400:
        break
    ans=min(ans,dp[Ma*i][Mb*i])
print(ans if ans!=INF else -1)