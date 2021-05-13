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


def dfs(n):
    global MOD
    var = 1
    isLeaf = True
    for e in edge[n]:
        if status[e] == 0:
            isLeaf &= False
            status[e] = 1
            var *= dfs(e)
            var %= MOD
    if isLeaf:
        ans = 1
    else:
        ans = nPk(K - 2 + (n == 0), len(edge[n]) - 1 + (n == 0))
        ans *= var
        ans %= MOD
    Leaf[n] = ans
    return ans


def nPk(n, k):
    global MOD
    x1 = modFacts[n]
    x2 = invs[n - k]
    ans = x1 * x2
    return ans % MOD


N, K = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)


for i in range(N):
    if len(edge[i]) + 1 > K:
        print(0)
        exit()

modFacts, invs = prepare(K)


Leaf = [0] * N
status = [0] * N
status[0] = 1
result = dfs(0)

print((result * K) % MOD)
