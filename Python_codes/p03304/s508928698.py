n, m, d = [int(i) for i in input().split()]
print((m - 1) * (n - d) * ((d != 0) + 1) / (n ** 2))
