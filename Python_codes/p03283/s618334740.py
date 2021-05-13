n, m, Q = map(int, input().split())
A = [[0]*(n) for i in range(n)]
C = [[0]*(n+1) for i in range(n)]
for i in range(m):
    l, r = map(int, input().split())
    A[r-1][l-1] += 1

for i in range(n):
    a = A[i]
    c = C[i]
    for j in range(n):
        c[j+1] = c[j] + a[j]

for i in range(Q):
    p, q = map(int, input().split())
    ans = 0
    for i in range(p-1, q):
        ans+=C[i][q] - C[i][p-1]
    print(ans)
