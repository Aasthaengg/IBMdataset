import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(G, v, p, dist):
    """G: graph, v: vertex, p: parent"""
    # Loop for each child
    for c, d in G[v]:
        # Avoid multiple access to parent
        if c == p:
            continue
        dist[c] = dist[v] + d
        dfs(G, c, v, dist)


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))

    Q, K = map(int, input().split())
    x = [0] * Q
    y = [0] * Q
    for i in range(Q):
        x[i], y[i] = map(int, input().split())

    dist = [0] * N
    dfs(G, K-1, -1, dist)
    for i in range(Q):
        ans = dist[x[i]-1] + dist[y[i]-1]
        print(ans)


if __name__ == "__main__":
    main()
