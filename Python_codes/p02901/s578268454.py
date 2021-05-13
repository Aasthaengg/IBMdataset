import sys
input = sys.stdin.readline
N, M = map(int, input().split())

INF = 1<<30
dp = [INF]*(1<<N)
dp[0] = 0

K = []
for _ in [0]*M:
    a, b = map(int, input().split())
    *C, = map(int, input().split())
    h = 0
    for c in C:
        h ^= 1 << (c-1)
    
    for i in range(1<<N):
        nxt = i|h
        dp[nxt] = min(dp[nxt], dp[i]+a)

ans = dp[(1<<N)-1]
print(-1 if ans == INF else ans)
