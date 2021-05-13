n, m, l= map(int, raw_input().split())
A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(l)] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    a = map(int, raw_input().split())
    for j in range(m):
        A[i][j] = a[j]
for i in range(m):
    b = map(int, raw_input().split())
    for j in range(l):
        B[i][j] = b[j]
for i in range(n):
    ans = ""
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
        if(j == 0):
            ans += str(C[i][j])
        else:
            ans += " " + str(C[i][j])
    print(ans)