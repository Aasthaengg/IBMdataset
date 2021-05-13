n, m, d = map(int, input().split())
if not d == 0:
    x = 2 * (n - d) / pow(n, 2)
else:
    x = (n - d) / pow(n, 2)
print(x * (m - 1))