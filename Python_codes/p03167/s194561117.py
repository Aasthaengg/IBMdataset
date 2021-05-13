import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())
D = ((1,0),(0,1))

H,W  = LI()
dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
mp = [sys.stdin.readline().rstrip() for _ in range(H)]

dp[0][1] = 1
for i in range(1,H+1):
    for j in range(1,W+1):
        if mp[i-1][j-1] == '#': continue
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[-1][-1])