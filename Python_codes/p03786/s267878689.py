import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = N
    while True:
        res = A[0]
        cnt = 1
        flag = False
        for i in range(1, len(A)):
            a = A[i]
            if a > 2 * res:
                ans = min(ans, len(A) - i)
                A = [res + a] + A[i + 1:]
                flag = True
                break
            else:
                res += a
        if flag:
            continue
        else:
            break

    print(ans)
