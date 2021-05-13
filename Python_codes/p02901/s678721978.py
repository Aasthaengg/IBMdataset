N, M = map(int, input().split()) 
asl = []
for _ in range(M):
    a, b = map(int, input().split()) 
    cl = list(map(int, input().split())) 
    s = 0
    for c in cl:
        s += 1<<(c-1)
    asl.append([a,s])

INF = 10**8
dp = [INF]*(2**N)
dp[0] = 0
for i in range(2**N):
    for as_v in asl:
        a, s = as_v
        dp[i|s] = min(dp[i]+a ,dp[i|s])

ans = dp[2**N-1]
if ans == INF:
    print(-1)
else:
    print(ans)
