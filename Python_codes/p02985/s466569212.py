from collections import deque

N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N - 1)]

tree = [[] for _ in range(N + 1)]
for a, b in X:
    tree[a].append(b)
    tree[b].append(a)

MAX = 10 ** 5 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    
# Inverse factorial
finv = [0] * (MAX + 1)
finv[MAX] = pow(fac[MAX], MOD - 2, MOD)
for i in reversed(range(1, MAX + 1)):
    finv[i - 1] = finv[i] * i % MOD

def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD

visited = [False] * (N + 1)
visited[0] = True
visited[1] = True
stack = deque([1])
ans = K
while stack:
    u = stack.popleft()
    child_num = sum(not visited[v] for v in tree[u])
    ans *= comb(K - 1 - int(u != 1), child_num) * fac[child_num]
    ans %= MOD
    for v in tree[u]:
        if not visited[v]:
            visited[u] = True
            stack.append(v)

print(ans)
