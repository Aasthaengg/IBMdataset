#グラフの連結成分を調べる
def Graph(ab):
    G=[[] for i in range(n)]
    for a,b in ab:
        G[a-1].append(b)
        G[b-1].append(a)
    return G

#BFS
from collections import deque
def bfs(G, v, p):
    point = [0] * n
    q=deque()
    q.append((v, p))
    point[0] = c.pop(0)

    score = 0
    while q:
        #qの先頭を取り出す
        V, P = q.popleft()
        for next_v in G[V - 1]:
            if next_v == P:continue
            q.append((next_v, V))
            temp = c.pop(0)
            score += temp
            point[next_v - 1] = temp

    return point, score

n = int(input())
ab = [list(map(int,input().split())) for i in range(n - 1)]
c = list(map(int,input().split()))
c = sorted(c, reverse=True)
G = Graph(ab)

point, score = bfs(G, 1, -1)
print(score)
print(*point)