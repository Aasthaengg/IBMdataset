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


def bellman_ford(edges, num_v, sv):
    #グラフの初期化
    dist = [INF] * num_v
    dist[sv] = 0
    
    #辺の緩和
    for i in range(num_v - 1):
        for edge in edges:
            s, t, d = edge[0], edge[1], edge[2]
            if dist[s] != INF and dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
    
    return dist


def main():
    N, M = map(int, input().split())

    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1; b -= 1; c *= -1
        edges.append([a, b, c])
    
    dist = bellman_ford(edges, N, 0)

    negative = [False]*N
    for _ in range(N):
        for edge in edges:
            s, t, d = edge[0], edge[1], edge[2]
            if dist[s] == INF:
                continue
            if dist[t] > dist[s] + d:
                dist[s] = dist[t] + d
                negative[t] = True
            if negative[s] == True:
                negative[t] = True

    if negative[N-1] == True:
        print("inf")
    else:
        print(-dist[N-1])


if __name__ == '__main__':
    main()
