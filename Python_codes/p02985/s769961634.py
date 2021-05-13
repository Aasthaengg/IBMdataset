import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
edges = [set() for _ in range(N+1)]
MOD = 10 ** 9 + 7
for _ in range(N-1):
    a, b = lr()
    edges[a].add(b)
    edges[b].add(a)

roots = [None] * (N+1)
roots[1] = 1
que = deque([1])
while que:
    q = que.popleft()
    for next in edges[q]:
        if roots[next] == None:
            roots[next] = q
            que.append(next)

def permutation(n, x):
    # nPx 順列　ex) permutaion(5, 2) = 20
    tmp = 1
    for i in range(n, n-x, -1):
        tmp = (tmp * i) % MOD
    return tmp

def dfs(x):
    global answer
    answer %= MOD
    if x == 1:
        answer *= permutation(K-1, len(edges[x]))
    else:
        answer *= permutation(K-2, len(edges[x])-1)
    for y in edges[x]:
        if y == roots[x]:
            continue
        dfs(y)

answer = K # 1にはK色塗れる
dfs(1)
print(answer%MOD)
# 50