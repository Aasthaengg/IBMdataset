N, M = map(int, input().split())
INF = 10 ** 7
A = list()
B = list()
C = list()
d = [[INF] * N for i in range(N)]
for m in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    C.append(c)
    d[a][b] = c
    d[b][a] = c
for k in range(N):
    d[k][k] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for m in range(M):
    if d[A[m]][B[m]] < C[m]:
        ans += 1

print(ans)

