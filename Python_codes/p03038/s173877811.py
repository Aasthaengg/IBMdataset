n, m = map(int, input().split())
a = list(map(int, input().split()))
d = []
e = 0; f = 0; g = 0
for _ in range(m):
    b, c = map(int, input().split())
    d.append([c, b])
a.sort()
d.sort(reverse=True)
for i in range(len(d)):
    for _ in range(d[i][1]):
        if a[e] < d[i][0]:
            a[e] = d[i][0]
        else:
            f = 1
            break
        e += 1
        if e == n:
            f = 1
            break
    if f == 1: break
for i in range(n): g += a[i]
print(g)