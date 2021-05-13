import numpy as np
from scipy.sparse.csgraph import floyd_warshall


def solve(N,L,edges,queries):

    graph = np.zeros((N,N),dtype=int)
    for a,b,c in edges:
        graph[a-1,b-1] = c
        graph[b-1,a-1] = c

    dist = floyd_warshall(graph, directed=False)
    dist = (dist<=L)
    dist = floyd_warshall(dist, directed=False)
    res = []
    for a,b in queries:
        d = dist[a-1,b-1]
        res.append(int(d-1) if d != float('inf') else -1)
    return res

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

if __name__ == '__main__':

    t = read().split()

    N,M,L = map(int,t[:3])

    m = map(int,t[3:M*3+3])
    edges = zip(m,m,m)

    Q = int(t[M*3+3])
    m = map(int, t[M*3+4:])
    queries = zip(m,m)

    print(*solve(N,L,edges,queries), sep='\n')