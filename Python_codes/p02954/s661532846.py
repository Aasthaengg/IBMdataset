import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

S = ns()
tmp = []
li = 'RL'
pre = 0
ct = 0
for now in S:
    if now == li[pre]:
        ct += 1
    else:
        tmp.append(ct)
        ct = 1
        pre = 1-pre
tmp.append(ct)
ans = []
for i in range(len(tmp)//2):
    l = tmp[2*i]
    r = tmp[2*i+1]
    if (l + r) % 2 == 0:
        m = (l + r) // 2
        for i in range(l-1):
            ans.append(0)
        ans.append(m)
        ans.append(m)
        for i in range(r-1):
            ans.append(0)
    else:
        m = (l + r) // 2
        if l % 2 == 1:
            for i in range(l-1):
                ans.append(0)
            ans.append(m+1)
            ans.append(m)
            for i in range(r-1):
                ans.append(0)
        else:
            for i in range(l-1):
                ans.append(0)
            ans.append(m)
            ans.append(m+1)
            for i in range(r-1):
                ans.append(0)
print(*ans)