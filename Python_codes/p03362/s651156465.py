import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N = NI()
p = []
for i in range(7,55555,10):
    for j in range(3,int(math.sqrt(i))+1):
        if i % j == 0: break
    else:
        p.append(i)

print(*p[:N])
