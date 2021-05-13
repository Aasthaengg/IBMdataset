H,W=map(int,input().split())
s=[0]*H
for i in range(H):
  s[i]= list(input())

dp= [[float("inf") for _ in range(W)] for _ in range(H)]
dp[0][0]= 1 if s[0][0]=="#" else 0

mv=[(-1,0),(0,-1)]
for i in range(H):
  for j in range(W):
    if i==0 and j==0: pass
    else:
      tmp=float("inf")
      for k in mv:
        a = i+k[0]
        b = j+k[1]
        if 0 <=a <= H-1 and 0 <=b <= W-1:
          if s[i][j]=="#" and s[a][b]==".":
            tmp= dp[a][b]+1
          else:
            tmp= dp[a][b]
        dp[i][j]=min(dp[i][j],tmp)
        
print(dp[-1][-1])