n, m, d = [int(item) for item in input().split()]
if d == 0:
    ans = (n - d) / (n * n) * (m - 1)
else:
    ans = (n - d) * 2 / (n * n) * (m - 1)
print(ans)