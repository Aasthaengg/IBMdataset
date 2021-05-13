s=input()
n=len(s)
# ある桁まで、ぴったり支払う時の解、+1円支払う時の解
# はじめは0円に対して考えるので、0と1。
dp=0,1
# 上からi+1桁目にたいして 
for i in range(n):
  si=int(s[i])
  # i+i桁目までぴったり払うときの最小値。ひとつ上の桁で+1払っているときは、繰り下がりを考慮。
  a=min(dp[0]+si,dp[1]+10-si)
  # i+1桁目までぴったり＋1を払う時の最小値。
  # つまり、次の桁に繰り下がりの1を残す。この桁における1は次の桁から見れば10。なのでdp[1]からの遷移には10が計算の項にある。
  b=min(dp[0]+si+1,dp[1]+10-(si+1))
  dp=a,b
print(dp[0])