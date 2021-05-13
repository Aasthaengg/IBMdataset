import sys
sys.setrecursionlimit(1000000)

N,M=map(int,input().split())

G=[[] for _ in range(N+1)]  #G[0]はダミー
for edge in range(M):
    x,y=map(int,input().split())
    G[x].append(y)

DP=[-1]*(N+1)   #DP[0]はダミー

def rec(now):
    global G
    global DP

    if DP[now]!=-1:
        return DP[now]

    else:
        res=0
        for next in G[now]:
            res=max(res,rec(next)+1)
        DP[now]=res
        return DP[now]  #resは不可


ans=0
for v in range(1,N+1):
    ans=max(ans,rec(v))



print(ans)



