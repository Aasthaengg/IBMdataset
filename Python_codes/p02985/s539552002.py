N, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

import queue
MOD = 10**9+7

def P(n, m, MOD=10**9+7):
    res = 1
    for i in range(m):
        res *= n - i
        res %= MOD
    return res

r = 0
dp = [1]*N

q = queue.Queue()
q.put((r, -1))
while not q.empty():
    v, p = q.get()
    if v == r: dp[v] = P(K-1, len(G[v]), MOD)
    elif len(G[v]) > 1: dp[v] = P(K-2, len(G[v])-1, MOD)
    for c in G[v]:
        if c == p: continue
        q.put((c, v))

ans = K
for n in dp:
    ans *= n
    ans %= MOD

print(ans)