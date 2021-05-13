import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    K = int(input())

    S = [s for s in S]
    D = [ord('z') - ord(s) + 1 if s != 'a' else 0 for s in S]
    T = []
    for s, d in zip(S, D):
        if d <= K:
            T.append('a')
            K -= d
        else:
            T.append(s)

    c = ord(T[-1])
    K %= 26
    for _ in range(K):
        if c == ord('z'):
            c = ord('a')
        else:
            c += 1
    T[-1] = chr(c)

    print(''.join(T))


if __name__ == '__main__':
    main()
