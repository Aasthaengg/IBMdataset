n, m = map(int, input().split())

n = (n + 2) if n == 1 else n
m = (m + 2) if m == 1 else m

print((n - 2) * (m - 2))