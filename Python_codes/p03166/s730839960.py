import sys
sys.setrecursionlimit(10**5+10)

N,M=map(int,input().split())

G=[[] for i in range(N)] #グラフを隣接リストで表現
for j in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    G[x].append(y)

dp=[-1]*N

def longest_path(v): #vを始点とした時の最長パスの長さ
    if dp[v] != -1: #更新済みの場合
        return dp[v]
    
    #更新されていなかった場合
    tmp_max = 0
    for u in G[v]:
        tmp_max = max(tmp_max,longest_path(u)+1)
    dp[v] = tmp_max #きちんとメモする
    
    return dp[v]

ans=0
for i in range(N):
    ans = max(ans,longest_path(i))

print(ans)