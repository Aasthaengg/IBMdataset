n, m = map(int, input().split())
x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    z.append(c)

ans = -1e18
for i in range(-1, 2, 2):
    for j in range(-1, 2, 2):
        for k in range(-1, 2, 2):
            v = []
            for l in range(n):
                v.append(x[l] * i + y[l] * j + z[l] * k)
            v.sort()
            v.reverse()
            now = 0
            for l in range(m):
                now += v[l]
            ans = max(ans, now)

print(ans)
