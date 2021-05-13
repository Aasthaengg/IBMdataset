#貰うDP, 集めるDP.
#配るDPはiからi+1/i+2を更新
n=int(input())
h=[int(x) for x in input().split()]
dp=[0]
f_inf=float('inf')
dp.extend([f_inf]*n)
#初期値: print(dp)
for i in range(1, n):
  #chmin
  dp[i]=min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
  if i>1:
    dp[i]=min(dp[i], dp[i-2]+abs(h[i]-h[i-2]))
print(dp[n-1])
#各足場までの最小コスト列: print(dp)