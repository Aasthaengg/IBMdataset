N = int(input())
P = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N+1)]

for p in P:
    dp[p] = dp[p-1]+1
    
print(N-max(dp))