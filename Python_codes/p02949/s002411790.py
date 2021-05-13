import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, P, *ABC = map(int, read().split())
    edge = [0] * M
    for i, (a, b, c) in enumerate(zip(*[iter(ABC)] * 3)):
        edge[i] = (a - 1, b - 1, -(c - P))

    dist = [INF] * N
    dist[0] = 0

    for _ in range(N - 1):
        for a, b, c in edge:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c

    for _ in range(N):
        for a, b, c in edge:
            if dist[b] != INF and dist[b] > dist[a] + c:
                dist[b] = -INF

    score = -dist[N - 1]

    if score == INF:
        print(-1)
    else:
        print(max(0, score))

    return


if __name__ == '__main__':
    main()
