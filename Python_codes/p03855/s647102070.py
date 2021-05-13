import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import Counter


n, k, l = map(int, input().split())

GRAPH = [[] for _ in range(n + 1)]
for _ in range(k):
    p, q = map(int, input().split())
    GRAPH[p].append(q); GRAPH[q].append(p)

def dfs(now):
    A[now] = a
    SEARCHED[now] = True
    for v in GRAPH[now]:
        if SEARCHED[v]:
            continue
        next = v
        dfs(next)

A = [0] * (n + 1)
SEARCHED = [False] * (n + 1)

a = 1
for i in range(1, n + 1):
    if SEARCHED[i]:
        continue
    dfs(i)
    a += 1

GRAPH = [[] for _ in range(n + 1)]
for _ in range(l):
    r, s = map(int, input().split())
    GRAPH[r].append(s); GRAPH[s].append(r)

def dfs(now):
    B[now] = b
    SEARCHED[now] = True
    for v in GRAPH[now]:
        if SEARCHED[v]:
            continue
        next = v
        dfs(next)

B = [0] * (n + 1)
SEARCHED = [False] * (n + 1)

b = 1
for i in range(1, n + 1):
    if SEARCHED[i]:
        continue
    dfs(i)
    b += 1

AB = [ab for ab in zip(A, B)]
COUNTS = Counter(AB)

for i in range(1, n + 1):
    print(COUNTS[AB[i]])
