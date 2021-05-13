N,K = map(int, input().split())
es = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    es[a-1].append(b-1)
    es[b-1].append(a-1)


MOD = 10**9+7
 
MAXN = N+5+K
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD
 

def nPr(n,r):
    if n < r:
        return 0
    return fac[n] * finv[n-r]


# 始点のノードがK個の色でぬれて、始点の子供がnPr(K-1, 始点の子の数)通りの塗り分け方がある。
# それらの子については、nPr(K-2, 子の数)の塗り方。

q  = []
used = [False] * N
used[0] = True
for nxt in es[0]:
    q.append(nxt)
    used[nxt] = True


ans = K * nPr(K-1, len(es[0]))
ans %= MOD
while q:
    curr = q.pop()
    ans *= nPr(K-2, len(es[curr]) - 1)
    ans %= MOD
    for nxt in es[curr]:
        if used[nxt]:
            continue

        used[nxt] = True
        q.append(nxt)


print(ans)