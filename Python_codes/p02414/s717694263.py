n, m, l = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
b = [[int(j) for j in input().split()] for i in range(m)]
c = [[sum([a[n][m] * b[m][l] for m in range(m)]) for l in range(l)] for n in range(n)]
for ans in c: print(*ans)
