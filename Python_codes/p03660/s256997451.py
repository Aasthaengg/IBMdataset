# ARC078D - Fennec VS. Snuke (ABC067D)
from collections import deque


def bfs(s: int, d: "List[int]") -> None:
    q = deque([s])
    while q:
        v = q.popleft()
        for u in G[v]:
            if not d[u]:
                q.append(u)
                d[u] = d[v] + 1


def main():
    global G, DB, DW
    N, *E = map(int, open(0).read().split())
    G = [[] for _ in range(N + 1)]
    for i in range(0, (N - 1) * 2, 2):
        v, u = E[i : i + 2]
        G[v] += [u]
        G[u] += [v]
    # DB, DW: distance from G[i] (black) and G[N] (white)
    DB, DW = [0] * (N + 1), [0] * (N + 1)
    bfs(1, DB), bfs(N, DW)
    b, w = 0, 0
    for i, j in zip(DB[1:], DW[1:]):
        if i <= j:
            b += 1
        else:
            w += 1
    flg = b > w
    print("Fennec" if flg else "Snuke")


if __name__ == "__main__":
    main()