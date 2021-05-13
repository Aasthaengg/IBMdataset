# https://atcoder.jp/contests/abc073/tasks/abc073_d

from itertools import permutations
from collections import defaultdict

N, M, R = map(int, input().split())
G = defaultdict(list)
d =[ [float("inf")] * N for i in range(N)]
listR = list(map(int, input().split()))
for _ in range(M):
    ai, bi, ci = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    G[ai].append((bi, ci))
    G[bi].append((ai, ci))
    d[ai][bi] = d[bi][ai] = ci

# わーしゃるふろいど
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

# print(d)

# 全てのpermutations (of R)を試す
ans = float("inf")
for perm in permutations(listR):
    cost_perm = 0
    for i in range(len(perm) - 1):
        pi, pj = perm[i] - 1, perm[i + 1] - 1
        cost_perm += d[pi][pj]
    ans = min(ans, cost_perm)
print(ans)