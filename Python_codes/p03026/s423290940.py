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


def bfs(N, v0, edge, C):

    search = [0] * N
    C = deque(C)
    search[v0] = C.popleft()
    q = deque()
    q.append(v0)

    while q:
        v = q.popleft()
        for nv in edge[v]:
            if search[nv] == 0:
                q.append(nv)
                search[nv] = C.popleft()

    return search


def main():

    N = in_n()
    ab = in_nl2(N - 1)
    edge = [[] for _ in range(N)]

    for i in range(N - 1):
        a, b = ab[i]
        a, b = a - 1, b - 1
        edge[a].append(b)
        edge[b].append(a)

    C = sorted(in_nl(), reverse=True)
    V = bfs(N, 0, edge, C)

    score = 0
    for i in range(N - 1):
        a, b = ab[i]
        a, b = a - 1, b - 1
        score += min(V[a], V[b])

    print(score)
    print(' '.join(map(str, V)))


if __name__ == '__main__':
    main()
