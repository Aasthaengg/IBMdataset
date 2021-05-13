n, m, d = map(int, input().split())
print('{:.10}'.format((n - d) * (2 if d != 0 else 1) / (n * n) * (m - 1)))