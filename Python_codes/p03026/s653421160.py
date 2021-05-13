import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0

def resolve():
    def dfs(v, p):
        global res
        c = C.pop(0)
        T[v] = c
        for u in edge[v]:
            if u == p:
                continue
            else:
                res += min(T[v], C[0])
                dfs(u, v)

    n = int(input())
    edge = [[] for _ in range(n)]
    cnt_edge = [0] * n
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
        cnt_edge[a - 1] += 1
        cnt_edge[b - 1] += 1
    C = list(map(int, input().split()))
    C.sort(reverse=True)

    start = cnt_edge.index(max(cnt_edge))

    T = [0] * n
    dfs(start, -1)
    print(res)
    print(*T)


if __name__ == '__main__':
    resolve()
