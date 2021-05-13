from sys import setrecursionlimit, stdin
import numpy as np

readline = stdin.readline
setrecursionlimit(10 ** 6)

def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t
  
def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j

N,M = map(int,readline().split())
parent = - np.ones(N,int)

for _ in range(M):
    A, B = map(lambda x: int(x) - 1, readline().split())
    unite(parent, A, B)

ans = 0
for i in range(N):
    if parent[i] < 0:
        ans += 1
print(ans-1)