n = int(input())
a = list(map(int, input().split()))
l = [0] * n
h = [0] * n

for i in range(n):
    if 0 <= i + a[i] < n:
        l[i + a[i]] += 1
    if 0 <= i - a[i] < n:
        h[i - a[i]] += 1

ans = 0
for ll, hh in zip(l, h):
    ans += ll * hh

print(ans)
