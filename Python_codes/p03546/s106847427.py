import sys
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
import numpy as np

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W = map(int, readline().split())
    L = list(list(map(int, readline().split())) for _ in range(10))
    A = list(list(map(int, readline().split())) for _ in range(H))
    dist = dijkstra(csr_matrix(L))
    ans = 0
    for a in A:
        for i in a:
            if i == -1:
                continue
            else:
                ans += dist[i][1]
    print(int(ans))




if __name__ == '__main__':
    main()
