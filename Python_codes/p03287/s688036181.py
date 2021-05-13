import sys,queue,math,copy,itertools,bisect,collections,heapq
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

N,M = LI()
A = itertools.accumulate(LI())

d = {0:1}
for x in A:
    m = x % M
    if m in d: d[m] += 1
    else: d[m] = 1

ans = 0
for x in d.values():
    ans += x * (x-1) // 2
print (ans)