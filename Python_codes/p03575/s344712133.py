import sys
import copy
sys.setrecursionlimit(10000)

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx != ry:
        par[rx] = ry

def same(x, y):
    return root(x) == root(y)


n, m = map(int, input().split())

par = [i for i in range(n)]

a = [0] * m
b = [0] * m

for i in range(m):
    a[i], b[i] = map(int, input().split())

ans = 0

for i in range(m):
    c = copy.deepcopy(a)
    d = copy.deepcopy(b)
    c = c[:i] + c[i+1:]
    d = d[:i] + d[i+1:]
    par = [i for i in range(n)]
    for j in range(m-1):
        unite(c[j]-1, d[j]-1)
    if not same(a[i]-1, b[i]-1):
        ans += 1

print(ans)