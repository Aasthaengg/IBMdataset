import sys

sys.setrecursionlimit(1000000)

N = int(input())
Nodes = [{} for i in range(N)]


def search(index, dist):
    neighbors = Nodes[index]
    for key in neighbors:
        if distances[key] is not None:
            continue

        distances[key] = dist + neighbors[key]
        search(key, distances[key])


# 木を作る
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Nodes[a][b] = c
    Nodes[b][a] = c

# 頂点Kから各点への距離を求める
Q, K = map(int, input().split())
distances = [None for i in range(N)]
distances[K-1] = 0
search(index=K-1, dist=0)

#print(distances)

# 解答
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    print(distances[x] + distances[y])
