#解説AC

import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

n,m=map(int,input().split())
es=[[] for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    es[x-1].append(y-1)

dp=[-1]*n

def memo(v):
    if dp[v]+1: #更新済 dp[v]!=-1
        return dp[v]
    a=0
    for i in es[v]:
        a=max(a,memo(i)+1)
    dp[v]=a
    return a

ans=0
for i in range(n):
    ans=max(ans,memo(i))

print(ans)
