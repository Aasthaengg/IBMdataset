from heapq import heappop, heappush
N,T = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(N)]
AB = sorted(AB)
#print(AB)
j = 0
ans=0
dp = [[0]*(T+1) for _ in range(N+1)]
for i in range(N):
  for t in range(T+1):
    dp[i+1][t]=max(dp[i+1][t],dp[i][t])
    if t<=T-1:
      dp[i+1][min(T,t+AB[i][0])]=max(dp[i+1][min(T,t+AB[i][0])],dp[i][t]+AB[i][1])
print(dp[N][T])
