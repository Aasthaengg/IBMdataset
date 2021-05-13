import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(v, p):
        global res
        for u in edge[v]:
            if u == p:
                continue
            col[u] = C.pop()
            res += min(col[v], col[u])
            dfs(u, v)

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    C = list(map(int, input().split()))
    C.sort()

    col = [0] * n
    col[0] = C.pop()
    dfs(0, -1)
    print(res)
    print(*col)


if __name__ == '__main__':
    resolve()
