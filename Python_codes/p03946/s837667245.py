n, t = map(int, input().split())
a = list(map(int, input().split()))

cmax = [0] * (n+1)
for i in reversed(range(n)):
    cmax[i] = max(a[i], cmax[i+1])

m = 10 ** 18
d = 0
ans = 0
for i in range(n):
    if d == cmax[i+1] - a[i]:
        ans += 1
    elif d < cmax[i+1] - a[i]:
        d = cmax[i+1] - a[i]
        ans = 1
print(ans)