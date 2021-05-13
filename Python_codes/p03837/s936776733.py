import sys
sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(M)]
    INF = float("inf")
    D = [[INF] * N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for a, b, c in ABC:
        D[a-1][b-1] = c
        D[b-1][a-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = M - sum(any(D[i][a-1] + c == D[i][b-1] for i in range(N)) for a, b, c in ABC)
    print(ans)


if __name__ == "__main__":
    main()