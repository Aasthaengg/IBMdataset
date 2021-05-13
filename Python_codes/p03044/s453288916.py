from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")
MOD = 1000000007


class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost


visited = []
vertex = []
def dfs(G, v, d):
    visited[v] = True
    if d % 2 == 0:
        vertex[v] = 0
    else:
        vertex[v] = 1

    for edge in G[v]:
        nv = edge.to
        if visited[nv]:
            continue
        nd = d + edge.cost
        dfs(G, nv, nd)


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, cost = map(int, input().split())
        a -= 1; b -= 1
        G[a].append(Edge(b, cost))
        G[b].append(Edge(a, cost))

    for _ in range(N):
        visited.append(False)
        vertex.append(0)
    
    dfs(G, 0, 0)

    for v in vertex:
        print(v)


if __name__ == '__main__':
    main()