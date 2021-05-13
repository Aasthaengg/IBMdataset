import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N, K, L = [int(x) for x in input().strip().split()]
road_par = [n for n in range(N)]
road_rank = [0 for _ in range(N)]
train_par = [n for n in range(N)]
train_rank = [0 for _ in range(N)]

def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]

def union(par, rank, x, y):
    x = find(par, par[x])
    y = find(par, par[y])
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for ｋ in range(K):
    p, q = [int(x) - 1 for x in input().strip().split()]
    union(road_par, road_rank, p, q)
for l in range(L):
    r, s = [int(x) - 1 for x in input().strip().split()]
    union(train_par, train_rank, r, s)

d = defaultdict(int)
for n in range(N):
    r = find(road_par, n)
    t = find(train_par, n)
    d[(r, t)] += 1

for n in range(N):
    print(d[(road_par[n], train_par[n])], end=' ')