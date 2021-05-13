N, K, *h = map(int, open(0).read().split())
h = sorted(list(h))
print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))
