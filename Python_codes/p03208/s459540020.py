N, K, *h = map(int, open(0).read().split())
h = sorted(list(h))
ans = float("inf")
for i in range(N - K + 1):
    ans = min(ans, h[i + K - 1] - h[i])
print(ans)
