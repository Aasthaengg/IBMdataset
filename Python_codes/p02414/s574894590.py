n, m, l = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(m):
    b.append(list(map(int, input().split())))
for i in range(n):
    li = [sum([a[i][j]*b[j][k] for j in range(m)]) for k in range(l)]
    print(' '.join(map(str, li)))

