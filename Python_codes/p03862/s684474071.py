n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s = a[0]
if a[0] > x:
    ans = (a[0] - x)
    s = x
for i in range(1, n):
    if a[i] + s > x:
        ans += ((a[i] + s) - x)
        s = x - s
    else:
        s = a[i]
print(ans)