import sys
from operator import itemgetter

read = sys.stdin.buffer.read
INF = 1 << 60


def main():
    N, M, *AB = map(int, read().split())

    Q = list(zip(*[iter(AB)] * 2))
    Q.sort(key=itemgetter(1))

    ans = 0
    last = 0
    for a, b in Q:
        if last < a:
            last = b - 1
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
