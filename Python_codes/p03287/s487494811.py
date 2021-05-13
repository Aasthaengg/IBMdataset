import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,M = LI()
A = LI()
A = list(itertools.accumulate(A))

d = {0:1}
for x in A:
    m = x % M
    if m in d:
        d[m] += 1
    else:
        d[m] = 1

ans = 0
for x in d.values():
    ans += x * (x-1) // 2
print (ans)