import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N = NI()

dp = [[[[0 for _ in  range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i == 0 and j == 2 and k == 1 or \
                i == 0 and j == 1 and k == 2 or \
                i == 2 and j == 0 and k == 1:
                dp[3][i][j][k] = 0
            else:
                dp[3][i][j][k] = 1

for x in range(4,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[x-1][i][j][k] == 0: continue
                    if j == 0 and k == 2 and l == 1 or \
                        j == 0 and k == 1 and l == 2 or \
                        j == 2 and k == 0 and l == 1: continue
                    if i == 0 and k == 2 and l == 1 or \
                        i == 0 and j == 2 and l == 1: continue
                    dp[x][j][k][l] = (dp[x][j][k][l] + dp[x-1][i][j][k]) % MOD

ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[-1][i][j][k]

print (ans % MOD)