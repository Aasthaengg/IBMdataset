# ABC143E - Travel by Car
def floyd_warshall(dist):
    """
    Compute the shortest paths of all pairs and modify dist.
    """
    V = len(dist)
    for i in range(V):  # intermediate point
        for j, c2 in enumerate(dist[j][i] for j in range(V)):  #  source
            for k, (c1, c3) in enumerate(zip(dist[j], dist[i])):  # target
                if c2 + c3 < c1:
                    dist[j][k] = c2 + c3


def main():
    # FW -> once more FW to edges <= L
    N, M, L, *X = map(int, open(0).read().split())
    ABC, ST = X[: 3 * M], X[3 * M + 1 :]
    INF = 1 << 60
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dist[i][i] = 0
    for v, u, cost in zip(*[iter(ABC)] * 3):
        dist[v][u] = dist[u][v] = cost
    floyd_warshall(dist)

    # assume distance within L as 1 and compute the number of fueling
    modified_dist = [[1 if x <= L else INF for x in d] for d in dist]
    floyd_warshall(modified_dist)
    ans = []
    for s, t in zip(*[iter(ST)] * 2):
        x = modified_dist[s][t]
        if x < INF:
            ans.append(x - 1)
        else:
            ans.append(-1)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()