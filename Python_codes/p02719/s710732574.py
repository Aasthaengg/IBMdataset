N, K = map(int, input().split())
if N >= K:
    print(min(N%K, abs(N%K-K)))
else:
    print(min(N, abs(N-K)))