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
    N = int(readline())
    A = list(list(map(int, readline().split())) for _ in range(N))
    A = np.array(A)
    D = dijkstra(A)
    if (A!=D).any():
        print(-1)
    else:
        ans = 0
        D += np.identity(N, int) * (10**10)
        for i in range(N):
            for j in range(i + 1, N):
                a = np.min(D[i] + D[j])
                if a > D[i, j]:
                    ans += D[i, j]
        print(int(ans))



if __name__ == '__main__':
    main()
