N, K = map(int, input().split())
a = [int(c) for c in input().split()]


dp = [False] * (K+1)
for k in range(K+1):
    for ai in a:
        if k >= ai:
            dp[k] = dp[k] or (not dp[k-ai])

print('First' if dp[k] else 'Second')