import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n):
        u, k, *V = map(int, input().split())
        for v in V:
            edge[u - 1].append(v - 1)

    depth = [f_inf] * n
    depth[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for u in edge[v]:
            if depth[u] == f_inf:
                depth[u] = depth[v] + 1
                que.append(u)

    for i in range(n):
        print(i + 1, depth[i] if depth[i] != f_inf else -1)


if __name__ == '__main__':
    resolve()

