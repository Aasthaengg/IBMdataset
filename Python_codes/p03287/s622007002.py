n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = (b[i] + a[i]) % m
b.sort()
ans = 0
c = b[0]
m = 0
for i in range(1, n + 1):
    if b[i] == c:
        m += 1
    else:
        c = b[i]
        m = 1
    if m >= 2:
        ans += m - 1
ans += b.count(0) - 1
print(ans)