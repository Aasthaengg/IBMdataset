import sys
import collections

from operator import itemgetter

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    AB = [[int(x) for x in input().split()] for _ in range(N)]

    C = []

    for i, (a, b) in enumerate(AB):
        C.append((a + b, i))

    C.sort(reverse=True)

    takahashi = 0
    aoki = 0
    for i in range(N):
        j = C[i][1]
        if i % 2 == 0:
            takahashi += AB[j][0]
        else:
            aoki += AB[j][1]

    print(takahashi - aoki)


if __name__ == '__main__':
    main()
