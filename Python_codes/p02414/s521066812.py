(n,m,l) = [int(x) for x in input().split()]
a = []
b = []
c = [[0 for x in range(l)] for y in range(n)]

for nc in range(n):
    a.append([int(i) for i in input().split()])

for mc in range(m):
    b.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]

for r in c:
    print(' '.join([str(d) for d in r]))