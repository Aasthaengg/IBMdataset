n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n-1):
    j = i + 1
    if j < n and a[i]+a[j] > x:
        d = min(a[j], (a[i]+a[j]) - x)
        a[j] -= d
        ans += d
    if a[i]+a[j] > x:
        d = min(a[i], (a[i]+a[j]) - x)
        a[i] -= d
        ans += d
print(ans)
