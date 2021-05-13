N = int(input())
A = list(list(map(int,input().split()))for _ in range(N))

c = [0]*(N)
p = []
for i in range(N):
    j = A[i][c[i]]-1
    if i == A[j][c[j]]-1 and i < j:
        p.append((i,j))
ans = 0
while p:
    q = []
    for i,j in p:
        c[i] += 1
        c[j] += 1
        if c[i] < N-1:
            k = A[i][c[i]]-1
            if A[k][c[k]]-1 == i:
                q.append((i,k))
        if c[j] < N-1:
            k = A[j][c[j]]-1
            if A[k][c[k]]-1 == j:
                q.append((j,k))
    ans += 1
    p = q[:]

if min(c) != N-1:
    print(-1)
else:
    print(ans)
