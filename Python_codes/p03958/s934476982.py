import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    K, T = map(int, input().split())
    A = list(map(int, input().split()))

    que = queue.PriorityQueue()
    for a in A:
        que.put(-a)

    que2 = queue.Queue()

    ans = 0
    while not que.empty():
        n = -que.get()
        if not que2.empty():
            que.put(que2.get())
        if que.empty():
            ans += 1
            if n - 1 > 0:
                n -= 1
                que.put(-n)
                continue
            else:
                break
        if n - 1 > 0:
            n -= 1
            que2.put(-n)

    print(ans - 1)
