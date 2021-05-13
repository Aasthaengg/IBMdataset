n = int(input())
s = n % 2
a = list(map(int, input().split()))
a.sort()
mi = a[0]
ma = a[n - 1]
l = []
for i in range(1, n - 1):
    if a[i] < 0:
        l.append((ma, a[i]))
        ma -= a[i]
    else:
        l.append((mi, a[i]))
        mi -= a[i]
l.append((ma, mi))
print(ma - mi)
for x, y in l:
    print(x, y)