import sys
input = sys.stdin.buffer.readline

n, k = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

mod = 10**9+7
N = 2*10**5
fac = [1]*(N+1)
finv = [1]*(N+1)
for i in range(N):
    fac[i+1] = fac[i] * (i+1) % mod
finv[-1] = pow(fac[-1], mod-2, mod)
for i in reversed(range(N)):
    finv[i] = finv[i+1] * (i+1) % mod

def prm(n, r, mod):
    if r <0 or r > n:
        return 0
    if r == 0:
        return 1
    return fac[n] * finv[n-r] % mod

s = [0]
visit = [-1]*n
visit[0] = 0
ans = 1
while s:
    v = s.pop()
    if v != 0:
        c = len(g[v])-1
        K = k-2
    else:
        c = len(g[v])+1
        K = k
    ans *= prm(K, c, mod)
    ans %= mod
    for u in g[v]:
        if visit[u] == -1:
            visit[u] = 0
            s.append(u)
print(ans)
