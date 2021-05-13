r, c = map(int, input().split())

a = []
for i in range(r):
    a.append(list(map(int, input().split())))
    a[i].append(sum(a[i]))

a.append([])
for j in range(c + 1):
    s = 0
    for i in range(r):
        s += a[i][j]
    a[-1].append(s)

for i, ai in enumerate(a):
    print(*ai)
