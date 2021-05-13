import sys
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    H, W = map(int, readline().split())
    L = list(list(map(int, readline().split())) for _ in range(10))
    path = dijkstra(csr_matrix(L))
    ans = 0
    for i in range(H):
        A = list(map(int, readline().split()))
        for j in range(W):
            a = A[j]
            if a!=-1:
                ans += path[a][1]
    print(int(ans))

if __name__ == '__main__':
    main()