n, x, *a = map(int, open(0).read().split())
a.sort()

ans = 0
for i in range(n - 1):
    if a[i] <= x:
        ans += 1
        x -= a[i]
if a[n - 1] == x:
    ans += 1
print(ans)
