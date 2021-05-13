n, m = map(int, input().strip().split())
a = [[0 for j in range(m)] for i in range(n)]
b = [[0] for j in range(m)]
c = [[0] for j in range(n)]

for i in range(n):
    a[i] = list(map(int, input().strip().split()))

for i in range(m):
    b[i] = [int(input())]


for i in range(n):
    for j in range(m):
        c[i][0] += a[i][j]*b[j][0]
    print(c[i][0])