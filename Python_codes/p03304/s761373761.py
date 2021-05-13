
n, m, d = [int(_) for _ in input().split()]
pt = n - d if d == 0 else (n - d) * 2
print((pt / (n ** 2)) * (m - 1))