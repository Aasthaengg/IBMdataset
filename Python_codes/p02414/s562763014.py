n, m, l = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    c.append([0 for k in range(l)])
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    b.append(list(map(int, input().split())))
for s in range(n):
    for t in range(l):
        elm = 0
        for u in range(m):
            elm += a[s][u] * b[u][t]
        c[s][t] = elm
for i in c:
    print(" ".join(map(str, i)))
