n, m, q = map(int, input().split())

x = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    x[a-1][b-1] += 1

for j in range(1, n):
    for k in range(n-j):
        x[k][j+k] += x[k][j+k-1] + x[k+1][j+k] - x[k+1][j+k-1]

for i in range(q):
    a, b = map(int, input().split())
    print(x[a-1][b-1])