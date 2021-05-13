import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [False]*(K+1)

for i in range(K+1):
    for ai in a:
        if i-ai>=0:
            dp[i] |= not dp[i-ai]

if dp[K]:
    print('First')
else:
    print('Second')