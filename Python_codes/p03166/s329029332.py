import sys
sys.setrecursionlimit(10**9)
N,M = map(int,input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    road[x].append(y)
flag = [0]*(N+1)
dist = [0]*(N+1)
def distance(i):#地点iから終点までの最長距離
    if flag[i] == 1:
        return dist[i]
    
    if road[i] == []:#行き先がない
        return 0
    else:#行き先がある
        long_dist = 0
        tmp = 0
        for dirct in road[i]:
            tmp = 1 + distance(dirct)
            long_dist = max(long_dist,tmp)
        flag[i]=1
        dist[i] = long_dist
        return long_dist

ans = 0
for i in range(1,N+1):
    ans = max(ans,distance(i))
print(ans)
