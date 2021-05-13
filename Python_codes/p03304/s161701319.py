n, m, d = map(int, input().split())
c = (n - 2 * d) * 2 + d * 2
if d == 0:
    c = n
print(c * (m - 1) / (n * n))