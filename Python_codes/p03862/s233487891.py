n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    total = a[i] + a[i + 1]
    if total > x:
        a[i] -= max(0, total - x - a[i + 1])
        a[i + 1] = max(0, a[i + 1] - (total - x))
    ans += max(total - x, 0)
print(ans)