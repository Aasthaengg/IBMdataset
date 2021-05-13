n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(m)]
Sum = []
key = 0
for i in range(n):
    Sum_s = []
    for j in range(l):
        key = 0
        for k in range(m):
            key += A[i][k] * B[k][j]
        Sum_s.append(key)
    Sum.append(Sum_s)
for i in range(n):
    for j in range(l - 1):
        print(Sum[i][j], end = ' ')
    print(Sum[i][l - 1])

