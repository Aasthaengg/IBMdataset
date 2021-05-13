import sys, bisect, math, itertools, string, queue, copy
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

l = []
n = inp()
for i in range(1, n+1):
    r = input().split()
    s = r[0]
    p = int(r[1])
    l.append([i, s, p])
ans = sorted(l, key=lambda x:(x[1], -x[2]))
for t in ans:
    print(t[0])
