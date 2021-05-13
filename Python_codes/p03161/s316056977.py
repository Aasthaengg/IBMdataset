N,K= list(map(int,input().split()))
hc=list(map(int,input().split()))
dp=[0]*N
for i in range(1,N):
  li=[abs(hc[i]-hc[j])+dp[j] for j in range( max(i-K,0),i) ]
  dp[i]=min(li)
print(dp[-1])