N, K = map(int, input().split())
stone = list(map(int, input().split()))
dp = [False]*(K+1)
for i in range(1,K+1):
    for k in range(N):
        if i >= stone[k]:
            if not dp[i-stone[k]]:
                dp[i] = True
print('First' if dp[K] else 'Second')