n,k=map(int,input().split())
lr=[]
for i in range(k):
  l_,r_=map(int,input().split())
  lr.append([l_,r_])
mod=998244353


#dp[i]=0からi-1マスからiのマスへ行く総数
dp=[0]*(n+1)
sumdp=[0]*(n+1)
#初期条件：マス0に最初いるので１通り
dp[1]=1
sumdp[1]=1
#dp漸化式
for i in range(2,n+1):
  for l,r in lr:
    if i>l:
      if i<=r:
        dp[i]=(dp[i]+sumdp[i-l])%mod
      else:
        dp[i]=(dp[i]+sumdp[i-l]-sumdp[i-r-1])%mod
  sumdp[i]=(sumdp[i-1]+dp[i])%mod
  
  
print(dp[n]%mod)

    

