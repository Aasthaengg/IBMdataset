n, m, l = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]

c = [[0 for i in range(l)] for i in range(n)]
for i in range(n):
    for j in range(l):
        c[i][j] = sum([(a[i][x] * b[x][j]) for x in range(m)])

for i in range(n):
    print(' '.join(map(str, c[i])))