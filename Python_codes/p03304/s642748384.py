print((lambda n, m, d: (m - 1) / (n * n) * (n if d == 0 else (2 * (n - d))))(*map(int, input().split())))