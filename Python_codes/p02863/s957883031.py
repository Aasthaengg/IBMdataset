N, T = map(int, input().split())
A = [None] * N
B = [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())


dp1 = [[0] * T for _ in range(N + 1)]
for i in range(N):
    for j in range(T):
        here = dp1[i][j]
        a, b = A[i], B[i]
        if j < a:
            dp1[i + 1][j] = here
        else:
            dp1[i + 1][j] = max(here, dp1[i][j - a] + b)

dp2 = [[0] * T for _ in range(N + 2)]
for i in range(N, 0, -1):
    for j in range(T):
        here = dp2[i + 1][j]
        a, b = A[i - 1], B[i - 1]
        if j < a:
            dp2[i][j] = here
        else:
            dp2[i][j] = max(here, dp2[i + 1][j - a] + b)

ans = 0
for i in range(1, N + 1):
    for j in range(T):
        n1 = dp1[i - 1][j]
        n2 = dp2[i + 1][T - 1 - j]
        last = B[i - 1]
        ans = max(ans, n1 + n2 + last)

print(ans)
