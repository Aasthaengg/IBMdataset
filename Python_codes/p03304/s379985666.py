n, m, d = [int(i) for i in input().split()]

if d == 0:
    print("{:.8f}".format((m - 1) / n))
else:
    print("{:.8f}".format((m - 1) * 2 * (n - d) / (n * n)))