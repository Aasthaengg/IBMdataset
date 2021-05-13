n, m = map(int, input().split())
a = [[0] * m for i in range(n)]
b = [0] * m
c = [0] * n
# read matrix A
for i in range(n):
    w = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = w[j]
# read vevtor b
for j in range(m):
    b[j] = int(input())
# Ab -> c
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
# output c
for i in range(n):
    print(c[i])