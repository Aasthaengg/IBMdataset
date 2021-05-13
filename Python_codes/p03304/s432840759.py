n, m, d = map(int, input().split())

if d == 0:
    print((m - 1.0) / n)
else:
    print((m - 1.0) * 2.0 * (n - d) / (n * n))