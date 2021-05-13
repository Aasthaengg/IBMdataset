import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, Q = map(int, readline().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, readline().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    P = [0] * N
    (*PX,) = map(int, read().split())
    for p, x in zip(*[iter(PX)] * 2):
        P[p - 1] += x

    stack = deque([0])
    seen = [False] * N
    while stack:
        v = stack.pop()
        seen[v] = True
        for nv in G[v]:
            if seen[nv]:
                continue
            P[nv] += P[v]
            stack.append(nv)

    print(' '.join(map(str, P)))
    return


if __name__ == '__main__':
    main()
