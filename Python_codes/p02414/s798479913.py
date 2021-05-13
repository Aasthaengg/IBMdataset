[n,m,l] = map(int,raw_input().split())
A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(l)] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    v = map(int,raw_input().split())
    for j in range(m):
        A[i][j] = v[j]
for i in range(m):
    v = map(int,raw_input().split())
    for j in range(l):
        B[i][j] = v[j]

for i in range(n):
    s = ''
    for j in range(l):
        for k in range(m):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
        if j == 0:
            s = str(C[i][j])
        else:
            s = s + ' ' + str(C[i][j])
    print s