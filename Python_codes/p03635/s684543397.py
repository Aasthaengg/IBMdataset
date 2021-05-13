n, m = map(int, input().split())
print((min(n, m) - 1) * (min(n, m) - 1) + abs(n - m) * (min(n, m) - 1))