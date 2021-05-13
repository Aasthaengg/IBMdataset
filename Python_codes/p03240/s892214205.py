n = int(input())

x = []
y = []
h = []
u = 0
for i in range(n):
    a = list(map(int, input().split(' ')))
    x.append(a[0])
    y.append(a[1])
    h.append(a[2])
    if h[i] > 0:
        u = i

for cx in range(101):
    for cy in range(101):
        H = abs(cx - x[u]) + abs(cy - y[u]) + h[u]
        ok = True
        for i in range(n):
            ok &= max(H - abs(cx - x[i]) - abs(cy - y[i]), 0) == h[i]
        if ok:
            print(cx, cy, H)
