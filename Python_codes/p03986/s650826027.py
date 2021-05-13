import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

x = ns()
ct = 0
ans = 0
for c in x:
    if c == 'S':
        ct += 1
    else:
        if ct > 0:
            ct -= 1
            ans += 2
print(len(x)-ans)
