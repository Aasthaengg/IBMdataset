# nPi mod
def permutation(n,i,mod):
    count = 1
    for _ in range(i):
        count = count * n % mod
        n -= 1
    return count

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int,input().split())
MOD = 10**9 + 7

# 頂点0から頂点N-1のN個
ab = [[int(i)-1 for i in input().split()] for _ in range(N-1)]

V = [[] for _ in range(N)]
for a,b in ab:
    V[a].append(b)
    V[b].append(a)

# 頂点nowの子ノードの数をchild[now]に格納
def dfs(now, before):
    count = 0
    for after in V[now]:
        if after == before:
            continue
        count += 1
        dfs(after, now)
    if count == 0:
        return
    else:
        child[now] = count

child = [0] * N
dfs(0,0)

answer = 1
for i in range(N):
    if i == 0:
        answer *= permutation(K-1, child[i], MOD)
    else:
        answer *= permutation(K-2, child[i], MOD)
    answer %= MOD

print(answer * K % MOD)