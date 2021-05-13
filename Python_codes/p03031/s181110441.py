N, M = [int(x) for x in input().split()]

X = [[0]*N for _ in range(M)]
for i in range(M):
    u = [int(x) for x in input().split()]
    k = u[0]
    for j in range(1, k + 1):
        X[i][u[j] - 1] = 1

p = [int(x) for x in input().split()]

ans = 0
for b in range(2**N):
    q = [0]*M
    for i in range(M):
        for j in range(N):
            if (b >> j) & 1:
                q[i] = (q[i] + X[i][j]) % 2
    if q == p:
        ans += 1

print(ans)