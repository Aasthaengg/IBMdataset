import sys
def input():
    return sys.stdin.readline()[:-1]
import math
from itertools import permutations, combinations
from collections import defaultdict

sys.setrecursionlimit(10**7)
N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N-1)]
mod = 10**9+7

edges = [[] for _ in range(N)]
for abi in ab:
    a, b = abi[0], abi[1]
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

max_edges = max(list(map(len, edges)))
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


res = K
def dfs(last, cur):
    global res

    if last == -1:
        for i, np in enumerate(edges[0]):
            res *= (K-i-1)
            res %= mod
            dfs(0, np)

    else:
        num_edges_cur = len(edges[cur]) - 1
        if num_edges_cur == 0:
            return
        i = 0
        for i in range(K-2, K-num_edges_cur-2, -1):
            res *= i
            res %= mod
        for np in edges[cur]:
            if np == last:
                continue
            else:
                dfs(cur, np)
        
dfs(-1, 0)

print(res)