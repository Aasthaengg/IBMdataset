import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,C = LI()
p = [[(0,0)] for _ in range(C+1)]
for _ in range(N):
    s,t,c = LI()
    p[c].append((s,t))

im = [0 for _ in range(10**5+1)]
for x in p:
    x.sort()
    for i in range(1,len(x)):
        s,t = x[i]
        if x[i-1][1] < s: s -= 1
        im[s] += 1
        im[t] -= 1

ans = 0
tm = 0
for t in im:
    tm += t
    ans = max(ans,tm)
print(ans)