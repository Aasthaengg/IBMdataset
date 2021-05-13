n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n - 1):
    ref = a[i] + a[i + 1]
    ans += max(ref - x, 0)
    if ref - x > 0:
        a[i + 1] = max(a[i + 1] - (ref - x), 0)

print(ans)