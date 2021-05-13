s='0'
s+=input()
n=len(s)
inf=float('inf')
dp=[[inf]*2 for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
  for j in range(2):
    si=int(s[-i-1])
    si+=j
    for a in range(10):
      ni=i+1
      nj=0
      b=a-si
      if b<0:
        nj=1
        b+=10
      dp[ni][nj]=min(dp[ni][nj],dp[i][j]+a+b)
print(dp[n][0])