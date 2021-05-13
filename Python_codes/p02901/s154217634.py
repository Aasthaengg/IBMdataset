# from pprint import pprint

N, M = map(int, input().split())
A = []
C = []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    c = map(lambda x: int(x)-1, input().split())
    state = 0
    for ci in c:
        state |= 1 << ci
    C.append(state)

INF = 10**18
dp = [[INF]*2**N for _ in range(M)]
dp[0][0] = 0

for i in range(M-1):
    for state in range(1 << N):
        used = state | C[i]
        cur = dp[i][state]
        if dp[i+1][used] > cur + A[i]:
            dp[i+1][used] = dp[i][state] + A[i]

        if dp[i+1][state] > cur:
            dp[i+1][state] = cur

ans = dp[-1][-1]
print(ans if ans != INF else -1)
