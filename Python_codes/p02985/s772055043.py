import sys
sys.setrecursionlimit(10 ** 6)


MOD = 10 ** 9 + 7


def prepare(n):
    global MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


def dfs(n, free):
    cnt = free
    rst = True
    for e in edge[n]:
        if status[e] == -1:
            cnt += 1
            status[e] = cnt
            rst &= dfs(e, 1)
    if cnt > K - 1:
        rst &= False
    return rst


N, K = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

modFacts, invs = prepare(K)


status = [-1] * N
status[0] = 0
result = dfs(0, 0)
if result:
    ans = 1
    for s in status:
        ans *= (K - s)
        ans %= MOD
else:
    ans = 0

print(ans)
