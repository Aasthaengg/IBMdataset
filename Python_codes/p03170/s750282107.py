import sys
read = sys.stdin.read
readline = sys.stdin.readline

N, K = map(int, readline().split())
a = list(map(int, readline().split()))

dp = [False] * (K + K + 1)
for i in range(K):
    if not dp[i]:
        for j in a:
            dp[i + j] = True

if dp[K]:
    print('First')
else:
    print('Second')