n, m, l = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(m):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += A[i][k] * B[k][j]
        print(s, end='')
        if j != l-1:
            print(' ', end='')
    print()