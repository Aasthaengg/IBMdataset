import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = float('inf')
dp = [INF] * (1 << N)
dp[0] = 0
for _ in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    bit = 0
    for i in c:
        bit += 1 << (i-1)
    for i in range(1 << N):
        dp[i | bit] = min(dp[i | bit], dp[i] + a)
print(dp[-1] if dp[-1] != INF else -1)
