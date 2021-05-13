N,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N-1)]
MOD = 10**9+7

es = [[] for i in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

MAXN = K+5
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def npr(n,r):
    if n<r: return 0
    return fac[n] * finv[n-r]


ans = K
stack = [(0,0)]
visited = [0]*N
while stack:
    v,d = stack.pop()
    visited[v] = 1
    c = 0
    for to in es[v]:
        if visited[to]: continue
        c += 1
        stack.append((to,d+1))
    if c==0: continue
    m = npr(K-1,c) if d==0 else npr(K-2,c)
    ans *= m
    ans %= MOD
print(ans)