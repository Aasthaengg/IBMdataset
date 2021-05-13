n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = t
for i in range(1, n):
    ans += t if a[i] - a[i-1] >= t else a[i] - a[i-1]
print(ans)
