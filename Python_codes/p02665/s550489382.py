import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    mi = [A[-1]]
    ma = [A[-1]]
    for i in reversed(range(n)):
        mi.append(math.ceil(mi[-1] / 2) + A[i])
        ma.append(ma[-1] + A[i])

    mi = mi[::-1]
    ma = ma[::-1]

    res = []
    for i in range(n + 1):
        if i == 0:
            if mi[i] <= 1 <= ma[i]:
                res.append(1)
                continue
            else:
                break

        if mi[i] <= (res[-1] - A[i - 1]) * 2 <= ma[i]:
            res.append((res[-1] - A[i - 1]) * 2)
        else:
            res.append(ma[i])

    print(sum(res) if len(res) != 0 else -1)


if __name__ == '__main__':
    resolve()
