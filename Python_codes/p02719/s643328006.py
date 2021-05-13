N,K = map(int, input().split())


min_N = 0
if N <= K:
    min_N = min(N, K - N)
else:
    min_N = N % K
    if min_N > abs(min_N - K):
        min_N = abs(min_N - K)
print(min_N)