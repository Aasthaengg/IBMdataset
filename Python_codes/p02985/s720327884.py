import sys

# import bisect
from collections import Counter, deque

# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math


# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class Edge:

    def __init__(self, index, u, v):
        self.index = index
        self.u = u
        self.v = v

    def __str__(self):
        return "{} {}".format(self.u, self.v)


class Vertex:

    def __init__(self, index):
        self.index = index
        self.connected_edge_index = []
        self.color = -1

    def __str__(self):
        return str(self.index)


class Graph:
    # 1-indexed

    def __init__(self, vertices=0):
        self.vertices = [Vertex(x) for x in range(vertices + 1)]
        self.edges = []
        self._vertex_count = vertices
        self._edges_count = 0

    def edges_count(self):
        return self._edges_count

    def vertices_count(self):
        return self._vertices_count

    def add_edge(self, u, v):
        edge = Edge(self._edges_count, u, v)
        self.vertices[edge.u].connected_edge_index.append(edge.index)
        self.vertices[edge.v].connected_edge_index.append(edge.index)
        self.edges.append(edge)
        self._edges_count += 1

    # 連結している節点を求める
    def neighbors(self, index):
        return [self.edges[e].u if self.edges[e].u != index else self.edges[e].v for e in
                self.vertices[index].connected_edge_index]

    # 連結要素数を求める
    def neighbors_count(self, index):
        return len(self.vertices[index].connected_edge_index)

    def __str__(self):
        desc = ""
        for i in range(self._edges_count):
            desc += str(self.edges[i]) + "\n"
        return desc


def main():
    n, k = list(map(int, readline().split()))
    g = Graph(n)

    for i in range(n-1):
        a, b = list(map(int, readline().split()))
        g.add_edge(a, b)

    que = deque()
    que.append((1, 0, k))

    while que:
        current, parent, c = que.popleft()
        g.vertices[current].color = c
        next_c = k - 1 - parent
        for i in g.neighbors(current):
            if g.vertices[i].color == -1:
                que.append((i, 1, next_c))
                next_c -= 1

    ans = 1

    for i in range(1, n + 1):
        ans *= g.vertices[i].color
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
