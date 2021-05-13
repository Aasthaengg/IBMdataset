n, m, l = map(int, input().split())
a = [[v for v in list(map(int, input().split()))] for i in range(n)]
b = [[v for v in list(map(int, input().split()))] for i in range(m)]
c = [[sum([a[j][x] * b[x][i] for x in range(m)]) for i in range(l)] for j in range(n)]
for i in range(n):
    print(' '.join(map(str, c[i])))