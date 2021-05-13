# https://atcoder.jp/contests/abc132/tasks/abc132_e
"""
タグ: bfs、拡張グラフ
"""

import sys
input = sys.stdin.readline
from collections import deque


class Graph:
    def __init__(self, n, directed=False, decrement=True, destroy=False, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.destroy = destroy
        self.edges = [set() for _ in range(self.n)]
        self.visited = set()
        self.info = [-1]*self.n
        for x, y in edges:
            self.add_edge(x,y)

    def add_edge(self, x, y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges[x].add(y)
        if self.directed == False:
            self.edges[y].add(x)

    def add_adjacent_list(self, i, adjacent_list):
        if self.decrement:
            self.edges[i] = set(map(lambda x: x - 1, adjacent_list))
        else:
            self.edges[i] = set(adjacent_list)

    def bfs(self, start=1, goal=-1, time=0, save=False):
        """
        :param start: スタート地点
        :param goal: ゴール地点
        :param save: True = 前回の探索結果を保持する
        :return: （ループがあっても）最短距離。存在しなければ -1
        """
        if self.decrement:
            start -= 1
            goal -= 1
        p, t = start, time
        self.visited.add((p,0))
        next_set = deque([(p, t)])
        while next_set:
            p, t = next_set.popleft()
            for q in self.edges[p]:
                if (q, (t+1)%3) in self.visited:
                    continue
                if q == goal and (t+1)%3==0:
                    return (t+1)//3
                self.visited.add((q,(t+1)%3))
                next_set.append((q, t + 1))
        return -1

##################################################################################################

N, M = map(int, input().split())
graph = Graph(N, directed=True, decrement=True, destroy=False)
for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x, y)
S, T = map(int, input().split())
print(graph.bfs(start=S, goal=T))

