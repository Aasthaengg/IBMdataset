n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
now = a[0]
if now > x:
    ans += now - x
    now = x
for i in a[1:]:
    tmp = max(0, now + i - x)
    now = i - tmp
    ans += tmp
print(ans)