from collections import defaultdict
INF = 10**13
N, M = map(int, input().split())
A = []
C = []
for m in range(M):
    a, b = map(int, input().split())
    A += [a]
    c = list(map(int, input().split()))
    C += [sum(map(lambda x: 2**(x-1), c))]
dp = [INF for i in range(2**N)]
dp[0] = 0
for i in range(2**N):
    for j in range(M):
        dp[i | C[j]] = min(dp[i] + A[j], dp[i | C[j]])

if dp[2**N-1] == INF:
    print(-1)
else:
    print(dp[2**N-1])