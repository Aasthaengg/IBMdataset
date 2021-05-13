import sys
import math
import collections
import bisect
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline().rstrip())
ns = lambda: map(int, sys.stdin.readline().rstrip().split())
na = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().rstrip().split()))


# ===CODE===

def main():
    n = ni()
    e = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = ns()
        a, b = a - 1, b - 1
        e[a].append(b)
        e[b].append(a)

    dist_f = [-1 for _ in range(n)]
    dist_s = [-1 for _ in range(n)]
    dist_f[0] = 0
    dist_s[n - 1] = 0

    def bfs(que, dist):
        while que:
            q = que.popleft()
            for ei in e[q]:
                if dist[ei] == -1:
                    dist[ei] = dist[q] + 1
                    que.append(ei)
        return dist

    dist_f = bfs(collections.deque([0]), dist_f)
    dist_s = bfs(collections.deque([n - 1]), dist_s)

    f = 0
    s = 0
    for df, ds in zip(dist_f, dist_s):
        if df <= ds:
            f += 1
        else:
            s += 1

    print("Fennec" if f > s else "Snuke")


if __name__ == '__main__':
    main()
