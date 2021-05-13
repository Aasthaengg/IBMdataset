x, y, z, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse = True)
b = sorted(list(map(int, input().split())), reverse = True)
c = sorted(list(map(int, input().split())), reverse = True)
d = []
e = []
for m in range(x):
    for n in range(y):
        d.append(a[m]+b[n])
d.sort(reverse = True)
for m in range(z):
    for n in range(min(3000, len(d))):
        e.append(c[m]+d[n])
e.sort(reverse = True)
for n in range(k):
    print(e[n])