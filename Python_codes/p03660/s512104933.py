import sys
from collections import deque

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def bfs(N, v0, edge):

    search = [-1] * N
    search[v0] = 0
    q = deque()
    q.append(v0)

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if search[nv] == -1:
                q.append(nv)
                search[nv] = search[v] + 1

    return search


def bfs2(N, v0, edge, dis):

    q = deque()
    q.append(v0)

    ret = []

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if dis[v] > dis[nv] and dis[nv] != 0:
                q.append(nv)
                ret.append(nv)

    return ret[::-1]


def bfs3(N, v0, edge, color, x):

    search = [False] * N
    search[v0] = True
    q = deque()
    q.append(v0)

    ret = 0

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if not search[nv]:
                if color[nv] == -1:
                    ret += 1
                    q.append(nv)
                elif color[nv] == x:
                    q.append(nv)
                search[nv] = True

    return ret


def main():

    N = in_n()
    edge = [[] for _ in range(N)]

    for i in range(N - 1):
        a, b = in_nn()
        a, b = a - 1, b - 1
        edge[a].append(b)
        edge[b].append(a)

    dis = bfs(N, 0, edge)
    color_v = bfs2(N, N - 1, edge, dis)

    color = [-1] * N
    color[0] = 1
    color[-1] = 0

    color_v = deque(color_v)
    teban = 1

    while color_v:

        if teban == 1:
            v = color_v.popleft()
            color[v] = 1
            teban = 0

        elif teban == 0:
            v = color_v.pop()
            color[v] = 0
            teban = 1

    fen = bfs3(N, 0, edge, color, 1)
    sun = bfs3(N, N - 1, edge, color, 0)

    # print(color, fen, sun)

    if teban == 1:
        if fen > sun:
            ans = 'Fennec'
        else:
            ans = 'Snuke'
    elif teban == 0:
        if sun > fen:
            ans = 'Snuke'
        else:
            ans = 'Fennec'

    print(ans)


if __name__ == '__main__':
    main()
