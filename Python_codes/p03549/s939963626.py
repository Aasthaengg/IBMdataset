n, m = map(int, input().split())

print((1900 * m + 100 * (n - m)) * (1 << m))
