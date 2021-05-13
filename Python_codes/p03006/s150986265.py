import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    XY = [[int(x) for x in input().split()] for _ in range(N)]

    c = collections.Counter()

    if N == 1:
        print(1)
        return

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            xi, yi = XY[i]
            xj, yj = XY[j]
            c[(xi - xj, yi - yj)] += 1

    print(N - c.most_common()[0][1])


if __name__ == '__main__':
    main()
