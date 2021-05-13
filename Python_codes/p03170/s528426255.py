N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (K+1)
for i in range(K):
    for a in A:
        if dp[i] == 0:
            if i + a <= K:
                dp[i+a] = 1

if dp[-1] == 0:
    print('Second')
else:
    print('First')
