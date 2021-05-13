import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        l, r, d = map(int, input().split())
        tree[l - 1].append([r - 1, d])
        tree[r - 1].append([l - 1, -d])

    def dfs(v, p):
        for u, d in tree[v]:
            if u == p:
                continue
            else:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + d
                    dfs(u, v)
                else:
                    if dist[u] != dist[v] + d:
                        print("No")
                        exit()

    dist = [f_inf] * n
    for i in range(n):
        if dist[i] == f_inf:
            dist[i] = 0
            dfs(i, -1)

    print("Yes")


if __name__ == '__main__':
    resolve()
