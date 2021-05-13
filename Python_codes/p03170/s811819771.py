N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (K+1)

for i in range(1, K+1):
    for j in range(N):
        if 0 <= i - a[j] and not dp[i-a[j]]:
            dp[i] = True
            break

print("First" if dp[K] else "Second")