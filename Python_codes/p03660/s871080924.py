# ABC067D - Fennec VS. Snuke (ARC078D)
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

from collections import deque


def bfs(s, d) -> None:
    q = deque([s])
    while q:
        v = q.popleft()
        for u in G[v]:
            if not d[u]:
                q.append(u)
                d[u] = d[v] + 1


def main():
    global G, DB, DW
    N = int(input())
    E = tuple(tuple(map(int, input().split())) for _ in range(N - 1))
    G = [[] for _ in range(N + 1)]
    for v, u in E:
        G[v] += [u]
        G[u] += [v]
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