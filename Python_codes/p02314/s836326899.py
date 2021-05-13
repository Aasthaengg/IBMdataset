N,M = map(int, raw_input().split())
C = map(int, raw_input().split())

INF = 10**9
DP = [INF]*(N+1)
DP[0] = 0

for i in range(1, N+1):
    for c in C:
        if c <= i:
            DP[i] = min(DP[i], DP[i-c]+1)

print DP[N]
