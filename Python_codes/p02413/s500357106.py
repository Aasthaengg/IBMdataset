r, c = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for y in range(r)]
b = []

for i in range(r):
    a[i].append(sum(a[i]))

for i in range(c):
    n = 0
    for j in range(r):
        n += a[j][i]
    b.append(n)

b.append(sum(b))
a.append(b)

for i in a:
    i = [str(x) for x in i]
    print(' '.join(i))