n=int(input())
c=[int(input()) for _ in range(n)]
color_sum=[0]*200001
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
color_sum[c[0]]+=1
# i個目まで考えたときの解。求めるのはdp[n]
# dp[i]:i個目より前で、i個目と同じ色の石があるところをjとして、dp[j-1]の和+dp[i-1]
for i in range(1,n): #二個目からn-1個目の計算をする。
  dp[i+1]=dp[i]
  if c[i]==c[i-1]:
    continue
  dp[i+1]+=color_sum[c[i]]
  color_sum[c[i]]=dp[i+1]
print(dp[n]%(pow(10,9)+7))