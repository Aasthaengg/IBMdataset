N = int(input())
A = [[]] + [list(map(int,input().split())) for _ in range(N)]

c = [0 for _ in range(N+1)]
p = []

for i in range(1, N+1):
    j = A[i][c[i]]
    if i==A[j][c[j]] and i<j:
        p.append((i,j))

ans = 0
while p:
    q = []
    for i,j in p:
        c[i] += 1
        c[j] += 1
        if c[i] < N-1:
            k = A[i][c[i]]
            if A[k][c[k]] == i:
                q.append((i,k))
        if c[j] < N-1:
            k = A[j][c[j]]
            if A[k][c[k]] == j:
                q.append((j,k))
    ans += 1
    p = q

ans = (ans if all(c[i]==N-1 for i in range(1, N+1)) else -1)
print(ans)