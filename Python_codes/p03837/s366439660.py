import heapq

N,M = map(int, input().split())
es = [[] for _ in range(N)]

for i in range(M):
    a,b,c = map(int, input().split())
    es[a-1].append((c, b-1))
    es[b-1].append((c, a-1))


"""
・ノード数が少ないので、全ノード間の最短距離を求めても間に合う
・ある辺eがいずれかの最短距離に含まれる　→　その辺eが結ぶ２ノードの最短距離はeの距離（それぞれの最短距離を束ねてある２ノードの最短距離を作るから）
"""

INF = float("inf")
# 全ノード間の最短距離を求める
d = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    q = []
    d[i][i] = 0
    heapq.heappush(q, (0, i))
    while q:
        cost, a = heapq.heappop(q)
        if d[i][a] < cost:
            continue
        for c,b in es[a]:
            if d[i][a] + c < d[i][b]:
                d[i][b] = d[i][a] + c
                heapq.heappush(q, (d[i][b], b))


# 全ての辺について、その辺の間の距離cがa->bまでの最短距離か確かめる
# ある辺がいずれかのノード間の最短経路に含まれるなら、その辺（が結ぶノード）も最短距離になるから。
cnt = 0
for i in range(N):
    for c, b in es[i]:
        if d[i][b] != c:
            cnt += 1

# 無向グラフなので２方向分カウントされてるから２で割る
print(cnt//2)