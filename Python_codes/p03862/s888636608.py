n, x = map(int, input().split())
a = list(map(int, input().split()))

last = a[0]
ans = 0
for i in range(1, n):
    if last + a[i] > x:
        num = last + a[i] - x
        ans += num
        last = max(0, a[i] - num)
    else:
        last = a[i]

print(ans)
