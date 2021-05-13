r,c = map(int,input().split())
a = []
for i in range(r):
    a.append(list(map(int,input().split())))
    a[i].append(sum(a[i]))
b = []
for i in range(c+1):
    x = [row[i] for row in a]
    b.append(sum(x))
a.append(b)
for x in a:
    print(*x)

