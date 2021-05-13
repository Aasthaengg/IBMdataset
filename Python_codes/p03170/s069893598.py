N, K = map(int, input().split())
arr = list(map(int, input().split()))
dp = [False]*(K+1)
for i in range(K+1):
    for k in range(N):
        if i >= arr[k] and not dp[i-arr[k]]:
            dp[i] = True
print('First' if dp[K] else 'Second')