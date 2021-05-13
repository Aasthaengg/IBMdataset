n,m=map(int,input().split())
up=float('inf')
dp=[[up]*(1<<n) for i in range(m)]
dp[0][0]=0
buy=[]
a=[]
for cnt in range(m):
    x,y=map(int,input().split())
    a.append(x)
    c=list(map(int,input().split()))
    tmp=0
    for w in c:
        tmp|=1<<(w-1)
    buy.append(tmp)
for i in range(m-1):
    for j in range(1<<n):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        dp[i+1][j|buy[i]]=min(dp[i][j]+a[i],dp[i+1][j|buy[i]]) #i番目を買っているよ
if dp[m-1][-1]==float('inf'):
    print(-1)
else:
    print(dp[m-1][-1])