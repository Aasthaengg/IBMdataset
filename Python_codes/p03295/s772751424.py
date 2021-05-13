import sys

read = sys.stdin.buffer.read
INF = 1 << 60


def main():
    N, M, *AB = map(int, read().split())

    Q = [[] for _ in range(N - 1)]
    for a, b in zip(*[iter(AB)] * 2):
        Q[a - 1].append(b - 2)

    min_y = INF
    ans = 0
    for i, ys in enumerate(Q):
        if ys:
            min_y = min(min_y, min(ys))
        if i == min_y:
            ans += 1
            min_y = INF

    print(ans)
    return


if __name__ == '__main__':
    main()
