import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

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
d = [0] * n
f = [0] * n
#print(g)
seen = [False] * n
s = 0
t = 0
def dfs(g, v):
    global t
    #print(v+1, t)
    if seen[v]:
        return
    seen[v] = True
    d[v] = t
    t += 1    
    for next_v in g[v]:
        #if seen[next_v]: continue
        dfs(g, next_v)
    f[v] = t
    t += 1
for i in range(n):
    if len(g[i]) != 0:
        dfs(g, i)
for i in range(n):
    print(i+1, d[i]+1, f[i]+1)


