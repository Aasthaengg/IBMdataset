import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    F = []
    for _ in range(N):
        f = list(map(int, input().split()))
        F.append(f)
    P = []
    for _ in range(N):
        p = list(map(int, input().split()))
        P.append(p)

    ans = -1000000000
    for am in range(2 ** 5):
        for pm in range(2 ** 5):
            opens = [0 for _ in range(10)]
            for i in range(5):
                if ((am >> i) & 1):
                    opens[2 * i] = 1
                if ((pm >> i) & 1):
                    opens[2 * i + 1] = 1
            if sum(opens) == 0:
                continue
            res = 0
            for i, fs in enumerate(F):
                cnt = 0
                for f, o in zip(fs, opens):
                    if f == 1 and o == 1:
                        cnt += 1
                res += P[i][cnt]
            ans = max(ans, res)

    print(ans)


if __name__ == '__main__':
    main()
