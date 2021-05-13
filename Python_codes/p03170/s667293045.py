import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())
N,K = LI()
a = LI()
dp = [0 for _ in range(K+1)]

for i in range(K,-1,-1):
    if dp[i]: continue
    for x in a: dp[i-x] = 1
if dp[0] == 1:
    print('First')
else:
    print('Second')