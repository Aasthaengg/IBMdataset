import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [0] * (N+1) # the max number using i matches
for i in range(N):
    if i > 0 and dp[i] == 0:
        continue
    for a in A:
        if i + cnt[a] > N:
            continue
        dp[i+cnt[a]] = max(dp[i+cnt[a]], dp[i]*10 + a)
print(dp[N])