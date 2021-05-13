import sys
sys.setrecursionlimit(10**7)


def dfs(start, dist, distance_list, explored):
    for node, cost in tree[start]:
        if explored[node] is False:
            explored[node] = True
            distance_list[node] = dist + cost
            dfs(node, distance_list[node], distance_list, explored)
    return distance_list


n = int(input())
tree = [[] for _ in range(n)]
distance = [float('inf') for _ in range(n)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append((b, c))
    tree[b].append((a, c))

q, k = map(int, input().split())
k -= 1
query = []
distance[k] = 0

for _ in range(q):
    x, y = map(int, input().split())
    query.append((x-1, y-1))

XX = [False for _ in range(n)]
XX[k] = True

X = dfs(k, 0, distance, explored=XX)

for i, j in query:
    print(X[i] + X[j])