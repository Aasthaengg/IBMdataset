n, m, d = map(int, input().split())
print([1/n, 2*(n - d)/n**2][d > 0] * (m - 1))