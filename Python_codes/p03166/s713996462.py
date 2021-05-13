#!python3

import sys
sys.setrecursionlimit(10 ** 6)

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()
XY = [LI() for _ in range(M)]

w = [None] * N
links = [[] for _ in range(N)]
visit = [False] * N


def create_links():
    for x, y in XY:
        links[x - 1].append(y - 1)


def dfs(u):
    visit[u] = True
    n = 0
    for v in links[u]:
        if not visit[v]:
            w[v] = dfs(v)
        n = max(n, w[v])
    return n + 1


def main():
    create_links()
    for i in range(N):
        if not visit[i]:
            w[i] = dfs(i)
    ans = max(w) - 1
    print(ans)


if __name__ == "__main__":
    main()
