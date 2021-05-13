n,k=map(int, input().split())
h=list(map(int,input().split()))
dp=[0]*(n)
if k+1<=n:
  max=k+1
else:
  max=n
  
for i in range(1,max):
  dp[i]=abs(h[0]-h[i])
 
for i in range(k,n):
  li=[abs(h[i]-h[ik])+dp[ik] for ik in range(i-1,i-k-1,-1) ]
  dp[i]=min(li)
  
print(dp[-1])