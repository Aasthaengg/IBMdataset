import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(now, vis, dis):
    for to,c in edge[now]:
        if not vis[to]:
            if dis[to] == 0:
                dis[to] = dis[now] + c
            else:
                dis[to] = min(dis[now] + c, dis[to])
            vis[now] = 1
            dfs(to, vis, dis)

N = int(input())

edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    edge[a-1].append([b-1, c])
    edge[b-1].append([a-1, c])

visited = [0]*N
distance = [0]*N

Q, K = map(int, input().split())
dfs(K-1, visited, distance)

#print(distance)

for _ in range(Q):
    x, y = map(lambda x:int(x)-1, input().split())
    print(distance[x]+distance[y])