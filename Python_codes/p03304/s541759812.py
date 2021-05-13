n, m, d = map(int, input().split())
print((n * (m - 1)) / (n ** 2) if d == 0 else ((n - d) * 2 * (m - 1)) / (n ** 2))
