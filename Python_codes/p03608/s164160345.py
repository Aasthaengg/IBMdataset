import sys
input = sys.stdin.readline
from itertools import permutations

def warshall_floyd(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def main():
    N, M, R = map(int, input().split())
    A = [int(i)-1 for i in input().split()]
    inf = float('inf')
    G = [[inf] * N for _ in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a][b] = min(G[a][b], c)
        G[b][a] = min(G[b][a], c)
    warshall_floyd(G)
    ans = float('inf')
    for perm in permutations(A, R):
        tmp = 0
        for i in range(R-1):
            tmp += G[perm[i]][perm[i+1]]
        ans = min(ans, tmp)
    print(ans)
    

if __name__ == '__main__':
    main()