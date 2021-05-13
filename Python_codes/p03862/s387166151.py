n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
if a[0]>x:
    ans = a[0]-x
    a[0] = x
for i in range(1, n):
    if a[i-1]+a[i]>x:
        tmp = a[i-1]+a[i]-x
        a[i] -= tmp
        ans += tmp
print(ans)