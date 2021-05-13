n, k = map(int, input().split())
h = sorted(int(input()) for _ in range(n))
print(min(r - l for l, r in zip(h[: 1 - k], h[k - 1 :])))