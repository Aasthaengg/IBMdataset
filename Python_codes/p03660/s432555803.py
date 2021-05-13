# ABC067D - Fennec VS. Snuke (ARC078D)
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(v: int, x: int, d: "List[int]") -> None:
    d[v] = x
    for u in G[v]:
        if not d[u]:
            dfs(u, x + 1, d)


def main():
    global G, DB, DW
    N = int(input())
    E = tuple(tuple(map(int, input().split())) for _ in range(N - 1))
    G = [[] for _ in range(N + 1)]
    for v, u in E:
        G[v] += [u]
        G[u] += [v]
    DB, DW = [0] * (N + 1), [0] * (N + 1)
    dfs(1, 1, DB), dfs(N, 1, DW)
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