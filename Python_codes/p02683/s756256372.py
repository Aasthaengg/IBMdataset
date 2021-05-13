n, m, x = map(int, input().split())
C = []
A = []
ans = float("inf")
for _ in range(n):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])

for i in range(2**n):
    now = [0] * m
    ns = 0

    for j in range(n):
        if i&(1<<j):
            ns += C[j]

            for k in range(m):
                now[k] += A[j][k]

    if min(now) >= x:
        ans = min(ans, ns)

if ans == float("inf"):
    print(-1)
else:
    print(ans)