import sys,queue,math,copy,itertools,bisect,collections,heapq
LI = lambda : [float(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())
N = NI()
p = LI()
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(0,i+1):
        dp[i][j] = dp[i-1][j-1] * p[i-1] + dp[i-1][j] * (1-p[i-1])

print(sum(dp[-1][N//2+1:]))
