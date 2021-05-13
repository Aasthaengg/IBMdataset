import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    edge = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        edge[u].append((w, v))
        edge[v].append((w, u))

    q = deque()
    q.append(0)
    color = [-1 for _ in range(N)]
    color[0] = True

    # print(edge)

    while q:
        v = q.popleft()
        for w, nv in edge[v]:
            if color[nv] == -1:
                if w % 2 == 0:
                    color[nv] = color[v]
                else:
                    color[nv] = not color[v]
                q.append(nv)

    # print(color)
    for c in color:
        if c:
            print(0)
        else:
            print(1)


if __name__ == '__main__':
    solve()
