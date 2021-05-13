import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

from collections import deque
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
g = []
for i in range(n):
    t = na()
    u = t[0] - 1
    k = t[1]
    v = [x-1 for x in t[2:]]
    g.append(v)
dist = [-1] * n
que = deque()
dist[0] = 0
que.append(0)
while que:
    #print(que)
    v = que.popleft()
    for nv in g[v]:
        if dist[nv] != -1: continue
        dist[nv] = dist[v] + 1
        que.append(nv)

for i in range(n):
    print(i+1, dist[i])

