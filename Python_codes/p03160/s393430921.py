n=int(input())
h=list(map(int,input().split()))
dp=[0]*(len(h))
dp[1]+=abs(h[1]-h[0])
for i in range(len(h)-2):
  dp[i+2]+=min((abs(h[i+2]-h[i+1])+dp[i+1]),(dp[i]+abs(h[i+2]-h[i])))
print(dp[-1])
               

