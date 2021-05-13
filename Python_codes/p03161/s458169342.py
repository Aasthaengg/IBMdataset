N,K=map(int,input().split())

h=list(map(int,input().split()))
for i in range(101):
  h.append(0)
  
big=10**5+100
dp=[float('inf') for i in range(big)]

dp[0]=0

for i in range(N):
  for j in range(1,K+1):
    if dp[i+j] > dp[i] + abs(h[i+j]-h[i]):
      dp[i+j] = dp[i] + abs(h[i+j]-h[i])
      
print(dp[N-1])