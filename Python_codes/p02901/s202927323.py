n, m = map(int, input().split())

A = [0]*m
C = [0]*m
for i in range(m):
    a, b = map(int, input().split())
    A[i] = a
    cs = list(map(int, input().split()))
    c = 0
    for c_ in cs:
        c += 1 << (c_-1)
    C[i] = c

dp = [float('inf')]*(1 << n)
dp[0] = 0
for i in range(1 << n):
    for j in range(m):
        c = C[j]
        dp[i|c] = min(dp[i|c], dp[i]+A[j])

if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print(-1)