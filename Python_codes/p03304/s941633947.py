n, m, d = [int(i) for i in input().split()]
print((m - 1) * [1 / n, 2 * (n - d) / (n ** 2)][d!=0])
