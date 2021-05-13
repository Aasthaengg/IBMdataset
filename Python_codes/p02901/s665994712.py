# N = int(input())
N, M = [int(i) for i in input().split()]
key = []
for i in range(M):
    a, b = [int(_) for _ in input().split()]
    cs = [int(_) for _ in input().split()]
    s = 0
    for c in cs:
        c -= 1
        s |= 1 << c
    key.append([s, a])

INF = 10**9
dp = [INF for i in range(2**N)]
dp[0] = 0
for i in range(2**N):
    for j in range(M):
        t = i | key[j][0]
        cost = key[j][1]
        dp[t] = min(dp[t], dp[i] + cost)
ans = dp[-1]
if ans == INF:
    print(-1)
else:
    print(ans)

