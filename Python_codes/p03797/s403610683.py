n, m = map(int, input().split())
print([m // 2, n + (m - n * 2) // 4][n < m // 2])
