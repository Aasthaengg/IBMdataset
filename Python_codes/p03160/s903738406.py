from collections import defaultdict
dp = defaultdict(lambda:int(10**9))

N = int(input())
L = list(map(int, input().split()))
dp[0] = 0
for i in range(0, N):
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + abs(L[i+1] - L[i]))
        if i+2 < N:
            dp[i+2] = min(dp[i+2], dp[i] + abs(L[i+2] - L[i]))

print(dp[N-1])
