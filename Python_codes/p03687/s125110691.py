import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

d = []
s = ns()
que = collections.deque()
for c in s:
    if c not in d:
        d.append(c)

ans = inf
if len(d) == 1:
    print(0)
else:
    for c in d:
        t = copy.copy(s)
        for j in range(len(s) - 1):
            nt = []
            for i in range(len(t)-1):
                if c not in t[i:i+2]:
                    nt.append(t[i])
                else:
                    nt.append(c)
            if nt.count(c) == len(nt):
                ans = min(j+1, ans)
                break
            t = copy.copy(nt)
            
    print(ans)
