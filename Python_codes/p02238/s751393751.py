import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def dfs(start, graph, visited, time):
    visited[start][0] = time
    for next in range(len(graph[start])):
        if not graph[start][next]: continue
        if visited[next][0] != -1: continue
        time += 1
        time = dfs(next, graph, visited, time)
    else:
        time += 1
        visited[start][1] = time
    return time


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    G = [[False] * N for _ in range(N)]
    visited = [[-1, -1] for _ in range(N)]

    for n in range(N):
        u, k, *V = il()
        for v in V:
            G[n][v - 1] = True

    time = 0
    for n in range(N):
        if visited[n][0] != -1: continue
        time += 1
        time = dfs(n, G, visited, time)
    for n in range(N):
        print(n + 1, *visited[n])


if __name__ == '__main__':
    main()

