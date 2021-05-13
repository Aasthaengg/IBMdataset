
import numpy as np
from scipy.sparse.csgraph import  dijkstra
from scipy.sparse import csr_matrix

def resolve():
    N, X, Y = map(int, input().split())
    G = np.zeros((N+1, N+1), dtype=np.int64)
    for i in range(1, N):
        G[i, i+1] += 1
        G[i+1, i] += 1
    G[X, Y] += 1
    G[Y, X] += 1

    csr = csr_matrix(G)
    dist = dijkstra(csr)

    dic = {}
    for di in dist:
        for d in di:
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1
    for i in range(1, N):
        if i in dic:
            print(dic[i]//2)
        else:
            print(0)

if __name__ == "__main__":
    resolve()
