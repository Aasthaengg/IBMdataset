n, t, *a = map(int, open(0).read().split())

ans = a[-1] + t

for i in range(n - 1):
    ans -= max(0, a[i + 1] - a[i] - t)
print(ans)
