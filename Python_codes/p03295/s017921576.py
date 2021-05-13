import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,M = LI()
island = [0 for _ in range(N)]
req = [[] for _ in range(N)]
for _ in range(M):
    a,b = LI()
    req[a-1].append(b-1)

p = 1
ans = 0
for i in range(N):
    if island[i] > p:
        ans += 1
        p = island[i]
    for b in req[i]:
        island[b] = p+1
print (ans)


