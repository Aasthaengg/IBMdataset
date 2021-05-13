import sys
from _collections import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def Bellmanford(n, edges, r):  # r: 始点
    d = [INF] * n
    d[r] = 0

    for i in range(n):
        for (u, v, c) in edges:
            if d[u] != INF and d[u] + c < d[v]:
                d[v] = d[u] + c
                if i == n - 1 and v == n - 1:
                    return 'inf'

    return -d[n - 1]

def main():
    N, M = map(int, readline().split())
    edges = []
    for _ in range(M):
        u,v,c = map(int, readline().split())
        edges.append([u-1,v-1,-c])

    d = [INF]*N
    d[0] = 0
    for i in range(N-1):
        for j in range(M):
            u, v, c = edges[j]
            if d[u] != INF and d[u] + c < d[v]:
                d[v] = d[u] + c
    ans = d[N-1]

    negative_loop = [False]*N
    for i in range(N):
        for j in range(M):
            u, v, c = edges[j]
            if d[u] != INF and d[u] + c < d[v]:
                d[v] = d[u] + c
                negative_loop[v] = True
            if negative_loop[u]==True:
                negative_loop[v]=True

    if negative_loop[N-1]==True:
        print('inf')
    else:
        print(-ans)




if __name__ == '__main__':
    main()