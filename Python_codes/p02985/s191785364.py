import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7

def permutation(n, x, mod=10**9+7):
    # nPx 順列　ex) permutaion(5, 2) = 20
    tmp = 1
    for i in range(n, n-x, -1):
        tmp = (tmp * i) % mod
    return tmp

N, K = lr()
graph = [[] for _ in range(N+1)] # 1-indexed
for _ in range(N-1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

answer = K # rootの色の塗り方
answer *= permutation(K-1, len(graph[1])) % MOD
root = 1
stack = []
for child in graph[1]:
    if len(graph[child]) > 1:
        stack.append((child, 1))
while stack:
    cur, p = stack.pop()
    l = len(graph[cur])
    if l > 1:
        answer *= permutation(K-2, len(graph[cur])-1) % MOD
    for child in graph[cur]:
        if child == p:
            continue
        if len(graph[child]) > 1:
            stack.append((child, cur))
    answer %= MOD

print(answer%MOD)
# 10
