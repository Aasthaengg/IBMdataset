# ABC061D - Score Attack
import sys
input = sys.stdin.readline

def bellman_ford(N: int, M: int, E: "Array[Array[int]]") -> int or None:
    INF = float("inf")
    dist = [INF] * (N + 1)
    dist[1] = 0

    # relax edges
    for i in range(N):
        for v, u, w in E:  # w: positive -> -w
            if dist[v] - w < dist[u]:
                dist[u] = dist[v] - w
                if i == N - 1 and u == N:  # detect negative cycles
                    return None
    return dist[-1]


def main():
    # reverse weights -> shortest path problem containing negative cycles
    N, M = tuple(map(int, input().split()))  # vertices, edges
    E = tuple(tuple(map(int, input().split())) for _ in range(M))
    ans = bellman_ford(N, M, E)
    flg = ans is not None
    print(-ans if flg else "inf")


if __name__ == "__main__":
    main()