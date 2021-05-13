n, k = map(int, input().split())
res = (n - k) * (n - k + 1) // 2
for i in range(k + 1, n + 1):
    if i == 1:
        continue
    a, b = divmod(n - i, i)
    res += a * (i - k) + max(b - k + 1, 0)
print(res)