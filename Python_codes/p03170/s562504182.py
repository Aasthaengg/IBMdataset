N, K = map(int, input().split())
A = [int(i) for i in input().split()]
dp = [False] * (K + 1)

for i in range(1, K + 1):
    for a in A:
        if i >= a:
            dp[i] |= dp[i - a] ^ True
print('First' if dp[K] else 'Second')
