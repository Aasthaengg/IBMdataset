import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する


N,M = map(int,input().split())
to = [[] for i in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    to[x-1]+=[y-1]

dp = [-1 for i in range(N)] #node[i]からの最長経路長を記す -1で未決定を示す

def memo(i):
    if dp[i] != -1:
        return dp[i]
    a=0
    for j in to[i]:
        a=max(a, memo(j)+1)
    dp[i] = a
    return a

lp = 0
for i in range(N):
    lp = max(lp,memo(i))
print(lp)
