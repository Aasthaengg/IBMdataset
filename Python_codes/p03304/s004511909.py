n, m, d = map(int, input().split())

x = (m - 1) / n
y = 1
if d > 0:
    if n % 2 == 0:
        t = n // 2
        y = 1 - 2 * (d - t) / n
    else:
        t = (n + 1) // 2
        y = 1 - (2 * (d - t) + 1) / n

print(x * y)
