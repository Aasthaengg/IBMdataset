import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    S = input()

    counts = []
    if S[0] == '0':
        counts.append(0)
    cnt = 1
    for i in range(1, N):
        if S[i - 1] == S[i]:
            cnt += 1
        else:
            counts.append(cnt)
            cnt = 1
    counts.append(cnt)
    if S[0] == '0':
        counts.append(0)

    cumsum = [0 for _ in range(len(counts) + 1)]
    for i in range(0, len(counts)):
        cumsum[i + 1] = cumsum[i] + counts[i]

    res = 0
    for left in range(0, len(cumsum), 2):
        right = left + 2 * K + 1
        if right >= len(cumsum):
            right = len(cumsum) - 1
        res = max(res, cumsum[right] - cumsum[left])

    print(res)


if __name__ == '__main__':
    main()
