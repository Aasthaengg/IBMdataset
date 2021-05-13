# D - Score Attack
import sys
sys.setrecursionlimit(10 ** 9)

import numpy as np
from heapq import heappush, heappop

N, M, = map(int, input().split())
graph = [[] for _ in range(N+1)] # graph[0]は使わない

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, -c)) # ヒープ構造を使うためスコアと重みはマイナスの値

def dijkstra(start, co):
    INF = 10 ** 15
    dist = [INF] * (N+1) # dist[0]は使わない
    dist[start] = 0
    que = [(0, start, co)] # queではscoreを先頭に
    while que:
        score, place, count = heappop(que) # placeは現在地
        if score > dist[place]: # 前来た時より点数が悪いか、無限ループしている場合continue
            continue
        for next_node, weight in graph[place]:
            score2 = score + weight
            if next_node == N and count > 1000: # いくらでも大きくなる場合
                print('inf')
                exit()
            if dist[next_node] > score2 and count < 2000: # 点数が良くなるなら、データを更新
                dist[next_node] = score2
                heappush(que, (score2, next_node, count+1))
    return dist

d1 = np.array(dijkstra(1, 0))
print(-d1[N])
