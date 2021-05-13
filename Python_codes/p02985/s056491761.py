import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
MOD = 10**9+7

n, k = map(int, input().split())
g = [list() for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

cnt = [0] * n

def dfs(v, p):
    n_cnt = 1 if p == -1 else 2
    for nv in g[v]:
        if nv == p: continue
        cnt[nv] = n_cnt
        n_cnt += 1
        dfs(nv, v)

dfs(0, -1)
ans = 1

for x in cnt:
    ans *= max(0, (k - x))
    ans %= MOD

print(ans)
