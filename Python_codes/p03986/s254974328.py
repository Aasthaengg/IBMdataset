import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    X = input()

    que = queue.LifoQueue()
    cnt = 0
    rest_T = 0
    for x in X:
        if x == 'S':
            que.put(x)
            cnt += 1
        elif x == 'T' and cnt > 0:
            _ = que.get()
            cnt -= 1
        else:
            rest_T += 1

    print(rest_T + cnt)


if __name__ == '__main__':
    main()
