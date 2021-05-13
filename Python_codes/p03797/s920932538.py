n, m = map(int, input().split())
print(m // 2) if n * 2 > m else print(n + (m - 2 * n) // 4)
