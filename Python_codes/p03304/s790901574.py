n, m, d = map(int, input().split())

if d > 0:
    cnt = 2 * (n - d)
else:
    cnt = n
print((m-1) * cnt / pow(n, 2))