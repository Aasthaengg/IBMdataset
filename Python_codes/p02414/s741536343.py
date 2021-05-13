n, m, l = map(int, input().split())

A = []
B = []
C = [[] for i in range(n)]

for i in range(n):
    tmp_row = list(map(int, input().split()))
    A.append(tmp_row)

for i in range(m):
    tmp_row = list(map(int, input().split()))
    B.append(tmp_row)

for i in range(n):
    for j in range(l):
        ab = sum([A[i][k] * B[k][j] for k in range(m)])
        if j == (l - 1):
            print(ab)
        else:
            print(ab, end = ' ')