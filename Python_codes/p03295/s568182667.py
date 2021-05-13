import sys
from operator import itemgetter

read = sys.stdin.buffer.read
INF = 1 << 60


def main():
    N, M, *AB = map(int, read().split())

    Q = [0] * M
    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
        Q[i] = (a - 1, b - 1)

    Q.sort(key=itemgetter(1))

    ans = 0
    last = -1
    for a, b in Q:
        if last < a:
            last = b - 1
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
