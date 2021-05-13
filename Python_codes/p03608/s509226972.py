from itertools import permutations
import sys
input = sys.stdin.readline

def main():
    N, M, RR = map(int, input().split())
    R = list(map(int, input().split()))
    INF = float("inf")
    T = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = tuple(map(int, input().split()))
        T[a-1][b-1] = c
        T[b-1][a-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if T[i][j] > T[i][k]+T[k][j]:
                    T[i][j] = T[i][k]+T[k][j]
    ans = INF
    for rs in permutations(R):
        cost = 0
        for i in range(RR-1):
            cost += T[rs[i]-1][rs[i+1]-1]
        ans = min(ans, cost)
    print(ans)

if __name__ == "__main__":
    main()