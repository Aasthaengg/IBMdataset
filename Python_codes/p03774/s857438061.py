n, m = map(int, input().split())

a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

c = []
d = []
for i in range(m):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)

for j in range(n):
    l = []
    for i in range(m):
        l.append(abs(a[j] - c[i]) + abs(b[j] - d[i]))
    print(l.index(min(l)) + 1)