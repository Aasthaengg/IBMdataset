n, m, d = map(int, input().split())
if d == 0:
    ans = n * (m - 1) / (n * n)
else:
    ans = 2 * (n - d) * (m - 1) / (n * n)
print('{0:.10f}'.format(ans))
