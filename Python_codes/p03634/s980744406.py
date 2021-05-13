import sys
sys.setrecursionlimit(200000)


def dfs(node, dis, adj_list):

    for next, d in adj_list[node]:
        if dis[next] == float("inf"):
            dis[next] = dis[node] + d
            dfs(next, dis, adj_list)

    return


n = int(input())
adj_list = [[] for _ in range(n)]


for i in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

q, k = map(int, input().split())

k -= 1
dis = [float("inf")] * n
dis[k] = 0
dfs(k, dis, adj_list)

for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(dis[x] + dis[y])
