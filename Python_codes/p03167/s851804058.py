INF=float('inf')
mod=10**9+7

h,w=map(int,input().split())
G=[]
for _ in range(h):
  s=input()
  G.append(s)
  
dp=[[-INF for i in range(w+1)] for j in range(h+1)]
dp[1][1]=1

for i in range(1,h+1):
  for j in range(1,w+1):
    if G[i-1][j-1]=='#':
      continue
    if i==1 and j==1:
      continue
    dp[i][j]=max(0,dp[i-1][j])+max(0,dp[i][j-1])
    dp[i][j]%=mod
print(dp[h][w])