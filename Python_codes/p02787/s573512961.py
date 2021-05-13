h,n=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
inf=float('inf')
dp=[inf]*(h+1)
# dp[i]:ダメージiを与えるための最小魔力
dp[0]=0
for a,b in ab:
  # a:ダメージ,b:魔力
  ndp=[inf]*(h+1)
  ndp[0]=0
  for i in range(1,h+1):
    ndp[i]=min(dp[i],ndp[max(0,i-a)]+b)
  dp=ndp
print(dp[h])