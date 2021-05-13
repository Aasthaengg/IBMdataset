#A
inf = float("inf")
N,M = map(int,input().split())
C = list(map(int,input().split()))
C.sort()

dp = [inf for i in range(N+1)]
dp[0] = 0
for c in C:
    for p in range(c,N+1):
        dp[p] = min(dp[p],dp[p-c]+1)
        
print(dp[N])



