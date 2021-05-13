# 自力,配るイメージ
INF=float("inf")
def LI():return list(map(int,input().split()))
h,n=LI()
AB=[LI() for _ in range(n)]  
dp=[0]+[INF]*(h+11000) #max(a)<=10000
for i in range(0,h+1):
  for j,k in AB:
    dp[i+j]=min(dp[i+j],dp[i]+k)
print(min(dp[h:]))