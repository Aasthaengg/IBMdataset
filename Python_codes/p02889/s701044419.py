import sys
input = sys.stdin.readline


def calc(N, g):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])


def main():
    N, M, L = map(int, input().split())
    adj = [{} for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        adj[A-1][B-1] = C
        adj[B-1][A-1] = C
    dst = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dst[i][i] = 0
        for j in adj[i]:
            dst[i][j] = adj[i][j]
    calc(N, dst)
    ans = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        ans[i][i] = 0
        for j in range(i+1, N):
            if dst[i][j] <= L:
                ans[i][j] = 1
                ans[j][i] = 1
    calc(N, ans)
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        x = ans[s-1][t-1]
        print(-1 if x == float("inf") else x-1)


if __name__ == "__main__":
    main()
