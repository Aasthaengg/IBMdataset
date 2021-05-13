n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = max(a[0] - x, 0)
a[0] = min(a[0], x)
for i in range(1, n):
    ans += max(a[i - 1] + a[i] - x, 0)
    a[i] = min(x - a[i - 1], a[i])

print(ans)
