n, m, q = map(int, input().split())
d = [[0] * n for _ in range(n)]
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    for i in range(l + 1):
        d[i][r] += 1
for i in range(n):
    for j in range(1, n):
        d[i][j] += d[i][j-1]
for _ in range(q):
    p, q = map(int, input().split())
    print(d[p-1][q-1])