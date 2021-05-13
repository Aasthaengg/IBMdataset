import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        L, R, D = map(int, input().split())
        tree[L - 1].append((R - 1, D))
        tree[R - 1].append((L - 1, -D))

    def dfs(v):
        for u, d in tree[v]:
            if depth[u] == f_inf:
                depth[u] = depth[v] + d
                dfs(u)
            else:
                if depth[u] != depth[v] + d:
                    print("No")
                    exit()

    depth = [f_inf for _ in range(n)]
    for i in range(n):
        if depth[i] == f_inf:
            depth[i] = 0
            dfs(i)

    print("Yes")


if __name__ == '__main__':
    resolve()
