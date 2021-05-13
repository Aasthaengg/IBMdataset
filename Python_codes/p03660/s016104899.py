import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *AB = map(int, read().split())
    G = [[] for _ in range(N)]
    for a, b in zip(*[iter(AB)] * 2):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    dist1 = [-1] * N
    dist1[0] = 0
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist1[nv] == -1:
                dist1[nv] = dist1[v] + 1
                if nv != N - 1:
                    queue.append(nv)

    dist2 = [-1] * N
    dist2[N - 1] = 0
    queue = deque([N - 1])
    while queue:
        v = queue.popleft()
        for nv in G[v]:
            if dist2[nv] == -1:
                dist2[nv] = dist2[v] + 1
                if nv != 0:
                    queue.append(nv)

    F = S = 0
    for i, (d1, d2) in enumerate(zip(dist1, dist2)):
        if i in (0, N - 1):
            continue
        if d1 == -1:
            S += 1
        elif d2 == -1:
            F += 1
        elif d1 <= d2:
            F += 1
        else:
            S += 1

    if F > S:
        print('Fennec')
    else:
        print('Snuke')

    return


if __name__ == '__main__':
    main()
