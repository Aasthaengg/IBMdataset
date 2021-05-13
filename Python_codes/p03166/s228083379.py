import sys
sys.setrecursionlimit(10**5+100)

N,M=map(int,input().split())
G=[[] for _ in range(N)]
for _ in  range(M):
    xi,yi=map(int,input().split())
    G[xi-1].append(yi-1)

dp=[-1]*N #各ノードを始点とした時の最長経路

def rec(v):
    if dp[v]!=-1:
        return dp[v]
    
    res=0

    for nv in G[v]:
        res=max(res,rec(nv)+1)
    
    dp[v]=res
    return res

ans=0
for v in range(N):
    ans=max(ans,rec(v))
print(ans)