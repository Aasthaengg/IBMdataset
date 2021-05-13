N, M = map(int, input().split())
key = []
for i in range(M):
    a, b = map(int, input().split())
    s = 0
    C = list(map(int, input().split()))
    for c in C:
        c -= 1
        s |= 1 << c
    key.append((s, a))

dp = [float('inf')] * (1 << N)
dp[0] = 0
for s in range(1 << N):
    for i in range(M):
        t = s | key[i][0]
        cost = dp[s] + key[i][1]
        dp[t] = min(dp[t], cost)
ans = dp[-1]
if ans != float('inf'):
    print(ans)
else:
    print(-1)
