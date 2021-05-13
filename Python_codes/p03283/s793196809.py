import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,M,Q = LI()
city = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    l,r = LI()
    city[l][r] += 1

for i in range(1,N+1):
    s = 0
    for j in range(1,N+1):
        s += city[i][j]
        city[i][j] = s + city[i-1][j]

for _ in range(Q):
    p,q = LI()
    ans = city[q][q] - city[q][p-1] - city[p-1][q] + city[p-1][p-1]
    print (ans)


