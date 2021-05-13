n, m = map(int, input().split())
a = [None] * n
b = [None] * m
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(m):
    b[i] = int(input())
for i in range(n):
    c = 0
    for j in range(m):
        c += a[i][j] * b[j]
    print(c)
