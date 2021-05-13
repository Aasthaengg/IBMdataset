n,m,l=map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    c = []
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += a[i][k] * b[k][j]
        c.append(sum)
    print(" ".join(list(map(str, c))))

