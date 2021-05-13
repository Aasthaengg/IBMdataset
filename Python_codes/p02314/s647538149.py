N, M = map(int, input().split())   
C = list(map(int, input().split()))

dp = [0] + [float('inf')] * N

for c in C:
    for i in range(N+1):
        if i >= c:
            dp[i] = min(dp[i], dp[i-c]+1)
print(dp[-1])


