n, m = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(map(int, raw_input().split()))
b = [input() for j in range (m)]
c = 0
for i in range(n):
    for j in range(m):
        c += a[i][j] * b[j]
    print c
    c = 0