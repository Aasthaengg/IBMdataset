H,W=map(int,input().split())
p=10**9+7
ma=[]
dp=[[0]*(W+2) for j in range(H+2)]
an=[]
dp[1][1]=1
for i in range(H):
     ma.append(list(input()))
     for j in range(W):
         if i==j==0:
             continue
         if ma[i][j]=="#":
             dp[i + 1][j + 1]=0
         else:
             dp[i+1][j+1]=(dp[i][j+1]+dp[i+1][j])%p
print(dp[H][W])
#print(tin[an.index(ans)])
