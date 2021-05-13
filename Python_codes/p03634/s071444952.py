import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

dis = [ 0 for _ in range(n)]  # 距離
adj = [[] for _ in range(n)] # 隣接リスト

for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1;b-= 1
    adj[a].append([b, c])
    adj[b].append([a, c])

# v; 現在の頂点
# p; vの親
# d; 現在の距離
def dfs(v, p, d):
    dis[v] = d
    for i, c in adj[v]:
        if i == p:
            continue
        dfs(i, v, d+c)

q, k = map(int, input().split())
k -= 1

dfs(k, -1, 0)

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1;y -= 1
    print(dis[x] + dis[y])