import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def permutation(n, x, mod=10**9+7):
    # nPx 順列　ex) permutaion(5, 2) = 20
    tmp = 1
    for i in range(n, n-x, -1):
        tmp = (tmp * i) % mod
    return tmp

N, K = lr()
edges = [[] for _ in range(N+1)]
MOD = 10 ** 9 + 7

for _ in range(N-1):
    a, b = lr()
    edges[a].append(b)
    edges[b].append(a)

parent = [0] * (N+1)
stack = [1] # 1の頂点から
while stack:
    node = stack.pop()
    for x in edges[node]:
        if x == parent[node]:
            continue
        parent[x] = node
        stack.append(x)

answer = K
stack = [1]
while stack:
    node = stack.pop()
    if parent[node] == 0:
        answer *= permutation(K-1, len(edges[node]))
    else:
        answer *= permutation(K-2, len(edges[node])-1)
    for next in edges[node]:
        if next == parent[node]:
            continue
        elif len(edges[next]) >= 2:
            stack.append(next)
    answer %= MOD

print(answer)
# 48