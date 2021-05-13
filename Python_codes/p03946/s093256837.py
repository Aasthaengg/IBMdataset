n, t = map(int, input().split())
a = list(map(int, input().split()))

profit = -1
low = a[0]
for i in range(n):
    if a[i] < low:
        low = a[i]
    x = 0 if low > a[i] else a[i] - low
    if profit < x:
        profit = x

ans = 0
low = a[0]
for i in range(n):
    diff = a[i] - low
    if diff == profit:
        ans += 1
    if a[i] < low:
        low = a[i]

print(ans)